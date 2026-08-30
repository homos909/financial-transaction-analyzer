[English](#english) | [Tiếng Việt](#tiếng-việt)

---

## English

# Financial Transaction Analysis Tool

A Python command-line tool that reads accounting transaction data from Excel, automatically generates monthly summary reports, detects statistically anomalous transactions, and exports results as an Excel report and a chart.

### Features

- Reads transaction data from Excel (`.xlsx`) files
- Aggregates revenue/expense by month
- Detects anomalous transactions using a statistical threshold (`mean + 2 × standard deviation`)
- Calculates monthly profit and month-over-month percentage change
- Exports a multi-sheet Excel report: Summary, Anomalies, Profit
- Generates a bar chart comparing revenue and expenses by month

### Installation

```bash
pip install pandas numpy matplotlib openpyxl
```

### Usage

```bash
python phan_tich.py <path_to_excel_file>
```

Example:
```bash
python phan_tich.py giao_dich_mau.xlsx
```

This produces:
- `bao_cao_v2.xlsx` — Excel report with 3 sheets
- `bieudo.png` — bar chart of revenue/expenses by month

### Input data format

The input Excel file must contain at least these columns:

| date | description | account | amount |
|------|-------------|---------|--------|
| 2026-06-01 | Service revenue | Doanh thu | 10000000 |
| 2026-06-03 | Marketing expense | Chi phí | 2000000 |

### Code architecture

The code is organized into independent functions, each responsible for one processing step:

- `doc_du_lieu()` — reads and normalizes input data
- `tong_hop_theo_thang()` — aggregates by month and account type
- `phat_hien_bat_thuong()` — detects anomalies using statistical thresholds
- `tinh_loi_nhuan()` — calculates monthly profit and percentage change
- `xuat_excel()` — writes results to a multi-sheet Excel file
- `ve_bieu_do()` — visualizes the data as a chart

### Tech stack

- Python 3
- pandas, numpy — data processing and analysis
- matplotlib — visualization
- openpyxl — Excel read/write
- argparse — command-line argument parsing

### Roadmap

- Support additional input formats (CSV, Google Sheets)
- Allow the anomaly detection threshold to be configured via CLI argument
- Add unit tests for each processing function

---

## Tiếng Việt

# Công cụ Phân tích Chi phí & Doanh thu

Công cụ dòng lệnh (CLI) viết bằng Python, đọc file Excel giao dịch kế toán, tự động tổng hợp báo cáo theo tháng, phát hiện giao dịch bất thường bằng phương pháp thống kê, và xuất kết quả ra file Excel + biểu đồ.

### Tính năng

- Đọc dữ liệu giao dịch từ file Excel (`.xlsx`)
- Tổng hợp doanh thu/chi phí theo từng tháng
- Phát hiện giao dịch bất thường (số tiền vượt ngưỡng `trung bình + 2 × độ lệch chuẩn`)
- Tính lợi nhuận theo tháng và % thay đổi so với tháng trước
- Xuất báo cáo Excel gồm 3 sheet: Tổng hợp, Giao dịch bất thường, Lợi nhuận
- Vẽ biểu đồ cột so sánh doanh thu/chi phí theo tháng

### Cài đặt

```bash
pip install pandas numpy matplotlib openpyxl
```

### Cách sử dụng

```bash
python phan_tich.py <đường_dẫn_file_excel>
```

Ví dụ:
```bash
python phan_tich.py giao_dich_mau.xlsx
```

Chương trình sẽ tạo ra:
- `bao_cao_v2.xlsx` — file Excel báo cáo với 3 sheet
- `bieudo.png` — biểu đồ cột doanh thu/chi phí theo tháng

### Cấu trúc file dữ liệu đầu vào

File Excel cần có tối thiểu các cột:

| date | description | account | amount |
|------|-------------|---------|--------|
| 2026-06-01 | Thu tiền dịch vụ | Doanh thu | 10000000 |
| 2026-06-03 | Chi phí marketing | Chi phí | 2000000 |

### Kiến trúc code

Code được tổ chức thành các hàm độc lập, mỗi hàm đảm nhiệm một bước xử lý:

- `doc_du_lieu()` — đọc và chuẩn hoá dữ liệu đầu vào
- `tong_hop_theo_thang()` — tổng hợp theo tháng và loại tài khoản
- `phat_hien_bat_thuong()` — phát hiện giao dịch bất thường bằng thống kê
- `tinh_loi_nhuan()` — tính lợi nhuận và % thay đổi theo tháng
- `xuat_excel()` — ghi kết quả ra file Excel nhiều sheet
- `ve_bieu_do()` — trực quan hoá dữ liệu bằng biểu đồ

### Công nghệ sử dụng

- Python 3
- pandas, numpy — xử lý và phân tích dữ liệu
- matplotlib — trực quan hoá
- openpyxl — đọc/ghi file Excel
- argparse — xử lý tham số dòng lệnh

### Hướng phát triển tiếp theo

- Hỗ trợ nhiều định dạng file đầu vào (CSV, Google Sheets)
- Cho phép tuỳ chỉnh ngưỡng phát hiện bất thường qua tham số dòng lệnh
- Thêm unit test cho từng hàm xử lý
