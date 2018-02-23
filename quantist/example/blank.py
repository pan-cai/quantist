import talib
import pandas as pd
import numpy as np
# from jqdata import *
from sklearn import preprocessing
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import datetime
import matplotlib.pyplot as plt


data_path = "../data/pool/"
stock_data = pd.read_excel(data_path + 'sh2.xls').sort_index(ascending=False)
stock_data['date'] = pd.to_datetime(stock_data['date'])

start_date = list(stock_data['date'])[0]
end_date = list(stock_data['date'])[-1]
test_start_date = list(stock_data['date'])[100]
print(start_date, end_date)

result = []
feature = []
lable = [] # up:1,down:-1,flat:0
discrete_feateure = []

def get_feature_date(stock_data):
    close_prices = stock_data['close']
    open_prices = stock_data['open']
    high_prices = stock_data['high']
    low_prices = stock_data['low']
    volumes = stock_data['volume']
    sma_data = talib.SMA(close_prices)[-1] #Simple Moving Average (Overlap Studies)
    wma_data = talib.WMA(close_prices)[-1]
    mom_data = talib.MOM(close_prices)[-1]
    stck, stcd = talib.STOCH(high_prices, low_prices, close_prices)
    stck_data = stck[-1]
    stcd_data = stcd[-1]

    macd, macdsignal, macdhist = talib.MACD(close_prices)
    macd_data = macd[-1]
    rsi_data = talib.RSI(close_prices, timeperiod=10)[-1]
    willr_data = talib.WILLR(high_prices, low_prices, close_prices)[-1]
    cci_data = talib.CCI(high_prices, low_prices, close_prices)[-1]

    mfi_data = talib.MFI(high_prices, low_prices, close_prices, volumes)[-1]
    obv_data = talib.OBV(close_prices, volumes)[-1]
    roc_data = talib.ROC(close_prices)[-1]
    cmo_data = talib.CMO(close_prices)[-1]



