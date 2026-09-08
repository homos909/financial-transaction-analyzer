import pandas as pd 
from phan_tich import phat_hien_bat_thuong

def test_phat_hien_dung_giao_dich_bat_thuong():
    df = pd.DataFrame({
        'description': [f'GD{i}' for i in range(1, 10)] + ['GD_bat_thuong'],
        'amount': [100000, 110000, 95000, 105000, 98000,
                   102000, 97000, 108000, 101000, 5000000]
    })
    ket_qua = phat_hien_bat_thuong(df)
    assert len(ket_qua) == 1
    assert ket_qua.iloc[0]['description'] == 'GD_bat_thuong'

def test_khong_co_giao_dich_nao_bat_thuong_khi_du_lieu_deu_nhau():
    df = pd.DataFrame({
        'description': [f'GD{i}' for i in range(1, 10)] + ['GD_bat_thuong'],
        'amount': [100000]*10
    })
    ket_qua = phat_hien_bat_thuong(df)
    assert len(ket_qua) == 0
    # KHONG can dong assert ket_qua.iloc[0][...] o day
    # vi ket_qua rong (0 dong) -> khong co gi de lay ra ca    