# -*- coding: utf-8 -*-

# quantist
# 
# Copyright 2017-2018 Pan Liu
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
# by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Unless required

""" 
Author: liupan 
"""

"""
Description:Grid Trading Act
"""

import pandas as pd
import matplotlib.pyplot as plt

"""
 1 Get data from pool
"""

data_path = "../data/pool/sh.csv"
sh = pd.read_csv(data_path).sort_index(ascending=False)
sh.reset_index(inplace=True)
sh['date'] = pd.to_datetime(sh['date'])

print(len(sh["close"]))
print("---------------------------------------------------------------------------------")

"""
2 Construct dataform
Example:
    column:
        date open close p_change ... change_base close_front capital label retracement 
    basic calculate:
        p_change: 
            (today_close - yesterday_close)*100/today_close
        change_base: 
            (close_today - close_base)*100/close_today
            sh["basic_change"] = (sh["close"] - close_base_day)*100/sh["close"]
    basic_day data: 
        date,       open,    high,   close,      low,      volume,    price_change, p_change
        2014-12-10, 2855.94, 2946.707, 2940.006, 2807.678, 5128869.0, 83.737,        2.93
        drawdown=max（capital_base - capital）/capital_base
        retracement = （capital_base - capital）/capital_base
        label
            buy:1
            sell:-1
            no operate :0
        change_rate:(open_today - close_front)/open_today
        close_front:
            close price of deal day
            first close_front is  2940.006
            close_front is natative
    captival
        capital_base = 10,000,000
        account
        account balance = capital_base 
    strategy:
        rate of return:close price
        buying or sell:open price
        end trade:
            capital < 0
        buy--buy_rate(more than 3%)
        sell--sell_rate(less than -3%)
        first deal: 20% capital_base = 20%*open_base_day
        change_rate:(open_today - close_front)/open_today
        if change_rate < -3%:
            buy--- 1
            capital = captical - open_today*100
            close_front = close_today
        elif change_rate > 3%:
            sell---- -1
             capital = captical + open_today*100
             close_front = close_today
        else:
            no_handle 0
            capital = captical
            close_front = close_front
        
        
    other:
        
        
"""

"""
basic date

capital_base（起始资金）
commission（手续费）
    buycost
    sellcost
slippage（滑点）
    买入股票的交易价格调整为 S × (1 + value)
    卖出股票的交易价格调整为 S × (1 - value)  
 order(s, 100)
 
Capitcal & balance
share(1)---straddle(100)
max_history_window（回溯长度）

"""
"""
change_base:
    (sh["close"] - close_base)/sh["close"]
    Calculate the maximum retracement
close_font: closed price of latest trade
change_rate:rate between now and close_font
mark: 
    change_rate > sell_price, mark=1, sell
    change_rate < buy_price, mark=-1, buy
    others,                  mark=0, no handler 

Example data form   
        change_base  change_rate     close  close_font       date  mark      open  \
    0      0.000000    -0.029435  2940.006    2940.006 2014-12-10    -1  2855.940   
    1     -0.487500    -0.009497  2925.743    2925.743 2014-12-11    -1  2912.346        
"""

"""
initialization
"""

date_base = 2014 - 12 - 10
close_base = sh.ix[0, "close"]  # 2940.006
capital = 10000000
sh["balance"] = 10000000
sell_price = 0.3  # If change_rate > sell_rate, sell the stock
buy_price = -0.3  # If change_rate > sell_rate, sell the stock
sell_rate = 0.1  # count/balance???
buy_rate = 0.1  # count/balance???

buy_cost = 0.0003
sell_commission = 0.0013
min_cost = 5

sh["close_font"] = close_base
sh["mark"] = 0
change_base = 0
sh["change_base"] = change_base

"""
The first buy_price or sell_price row
"""
# row = 0, sh["change_base"] = change_base = 0
for row in range(len(sh["close"])):
    # sh["change_base"] = (sh["close"] - close_base) / sh["close"]
    if row == 0:
        sh["change_base"] = change_base
    else:
        sh["change_base"] = (sh["close"] - close_base) / sh["close"]

        if (sh.ix[row, "change_base"] > 0.03):

            #print(sh.ix[row, "change_base"])
            sh.ix[row, "close_font"] = sh.ix[row, "close"]  # test...
            sh.ix[row, "mark"] = 1
            #change_base = 0
            close_base = sh.ix[row, sh["close"]]
        else:
            # sh["change_base"] = (sh["close"] - close_base) / sh["close"]
            sh["change_base"] = (sh["close"] - close_base) / sh["close"]
            sh.ix[row, "mark"] = 0

            # break;

print("---------------------------------------------------------------------------------")

sh["change_rate"] = (sh["open"] - sh["close_font"]) / sh["open"]

"""
sh["change_base"] = (sh["close"] - close_base)/sh["close"]
#Calculate the maximum retracement
retracement_max = sh["change_base"].max()
retracement_min = sh["change_base"].min()
print(retracement_max, retracement_min,retracement_max-retracement_min)
print("---------------------------------------------------------------------------------")
"""

"""
# sh["mark"] = sh["change_rate"].map(lambda x: 1 if x>sell_price else (-1 if x<-buy_price else 0 ))
sh["mark_rate"] = 0
for row in range(len(sh["close"])):
    if (row == 0):
        sh.ix[row, "close_font"] = sh.ix[row, "close"]
        sh["mark_rate"] = 0


    elif (sh.ix[row, "mark"] == 1):
        sh.ix[row, "close_font"] = sh.ix[row, "close"]
    elif (sh.ix[row, "mark"] == -1):
        sh.ix[row, "close_font"] = sh.ix[row, "close"]

    else:
        sh.ix[row, "close_font"] = sh.ix[(row-1), "close_font"]
"""

print("---------------------------------------------------------------------------------")
result = {"date": sh["date"], "open": sh["open"], "close": sh["close"], "p_change": sh["p_change"],
          "close_font": sh["close_font"], "change_rate": sh["change_rate"], "change_base": sh["change_base"],
          "balance": sh["balance"], "mark": sh["mark"], "mark": sh["mark"]}
result = pd.DataFrame(result)

print(result[:100])
print("---------------------------------------------------------------------------------")
