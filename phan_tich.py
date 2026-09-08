import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse


def doc_du_lieu(duong_dan_file):
    """Đọc file Excel, thêm cột 'thang'. Trả về DataFrame."""
    df = pd.read_excel(duong_dan_file)
    df['date'] = pd.to_datetime(df['date'])
    df['thang'] = df['date'].dt.strftime('%Y-%m')
    return df


def tong_hop_theo_thang(df):
    """Tính tổng amount theo thang + account. Trả về DataFrame đã reset_index()."""
    tong_hop = df.groupby(['thang', 'account'])['amount'].sum().reset_index()
    return tong_hop


def phat_hien_bat_thuong(df):
    """Lọc ra các dòng có amount > trung_bình + 2*độ_lệch_chuẩn. Trả về DataFrame."""
    trung_binh = np.mean(df['amount'])
    do_lech_chuan = np.std(df['amount'])
    nguong_bat_thuong = trung_binh + 2 * do_lech_chuan
    bat_thuong = df[df['amount'] > nguong_bat_thuong]
    return bat_thuong


def xuat_excel(tong_hop, bat_thuong, loi_nhuan, ten_file_output):
    """Ghi 2 DataFrame vào 2 sheet của 1 file Excel."""
    with pd.ExcelWriter(ten_file_output) as writer:
        tong_hop.to_excel(writer, sheet_name ='Tong hop', index = False)
        bat_thuong.to_excel(writer, sheet_name ='Bat Thuong', index = False)
        loi_nhuan.to_excel(writer, sheet_name = 'Loi nhuan', index = True)


def ve_bieu_do(tong_hop, ten_file_anh):
    """Vẽ biểu đồ cột Doanh thu/Chi phí theo tháng, lưu ra file ảnh."""
    doanh_thu = tong_hop[tong_hop['account'] == 'Doanh thu']
    chi_phi = tong_hop[tong_hop['account'] == 'Chi phí']

    plt.figure(figsize=(8 ,5))
    plt.bar(doanh_thu['thang'], doanh_thu['amount'], label= 'Doanh thu', color='green', alpha=0.7)
    plt.bar(chi_phi['thang'], chi_phi['amount'], label= 'Chi phí', color='red', alpha=0.7, width=0.4)
    plt.xlabel('Tháng')
    plt.ylabel('Số tiền (VNĐ)')
    plt.title('Doanh thu và Chi phí theo tháng')
    plt.legend()
    plt.tight_layout()
    plt.savefig(ten_file_anh)
    print(ten_file_anh)

def tinh_loi_nhuan(tong_hop):
    pivot = tong_hop.pivot(index ='thang', columns ='account', values='amount')
    pivot['loi_nhuan'] = pivot['Doanh thu'] - pivot['Chi phí']
    pivot['thay_doi_loi_nhuan_%'] = pivot['loi_nhuan'].pct_change() * 100
    return pivot

def phat_hien_bat_thuong_iqr(df):
    """
    Loc ra cac dong bat thuong dua tren IQR (Interquartile Range),
    it bi anh huong boi outlier hon so voi mean + 2*std.
    """
    q1 = df['amount'].quantile(0.25)
    q3 = df['amount'].quantile(0.75)
    iqr = q3 - q1

    nguong_duoi = q1 - 1.5 * iqr
    nguong_tren = q3 + 1.5 * iqr

    bat_thuong = df[(df['amount'] < nguong_duoi) | (df['amount'] > nguong_tren)]
    return bat_thuong

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Công cụ demo argparse")
    parser.add_argument("ten_file", help="Đường dẫn tới file cần xử lý")
    args = parser.parse_args()
  
    df = doc_du_lieu(args.ten_file)
    tong_hop = tong_hop_theo_thang(df)
    bat_thuong = phat_hien_bat_thuong(df)
    loi_nhuan = tinh_loi_nhuan(tong_hop)

    xuat_excel(tong_hop, bat_thuong, loi_nhuan, "bao_cao_v2.xlsx")
    ve_bieu_do(tong_hop, "bieudo.png")
    print("Hoàn thành!")


#Commnet test