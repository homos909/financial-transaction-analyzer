import pandas as pd
from phan_tich import phat_hien_bat_thuong_iqr

def test_phat_hien_bat_thuong_iqr():
    df = pd.DataFrame({
    'description': ['GD1', 'GD2', 'GD3', 'GD4', 'GD_bat_thuong'],
    'amount': [100000, 110000, 95000, 105000, 5000000]
})    
    ket_qua = phat_hien_bat_thuong_iqr(df)
    assert len(ket_qua) == 1
    assert ket_qua.iloc[0]['description'] == 'GD_bat_thuong'