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
sh = pd.read_csv(data_path)
#print(sh[:3])


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
sh["change_base"] = (sh["close"] - 2940.006)*100/sh["close"]
#plt.show(plt.plot(sh["basic_change"]))
sh["capital"] = 10000000
sh["label"] = 1
sh["close_font"] = 2940.006
sh["change_rate"] = (sh["open"] - sh["close_font"])/sh["open"]
print(sh[0:3])


