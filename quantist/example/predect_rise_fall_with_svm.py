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
import quantist.global_list as gl


data_path = "../data/pool/"
stock_data = pd.read_excel(data_path + 'sh2.xls').sort_index(ascending=False)

stock_data = gl.TEST_CLOSE_PRICES

stock_data['date'] = pd.to_datetime(stock_data['date'])

start_date = list(stock_data['date'])[0]
end_date = list(stock_data['date'])[-1]
test_start_date = list(stock_data['date'])[100]
print(start_date, end_date)

close_prices = stock_data['close'].values
open_prices = stock_data['open'].values
high_prices = stock_data['high'].values
low_prices = stock_data['low'].values
volumes = stock_data['volume'].values

sma_data = talib.SMA(close_prices) #Simple Moving Average (Overlap Studies)
print(sma_data)
print(len(sma_data))

