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
Description:
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

close_base = sh.ix[0, "close"]
mark_buy = 1
close_buy = []
mark_sell = -1
close_sell = []
mark_no_hanler = 0
sh["change_base"] = 0
#print("change_base  ", "  mark", "p_change")
for row in range((len(sh["close"]))):
    sh.ix[row,"change_base"] = (sh.ix[row,"close"] - close_base) / sh.ix[row, "close"]
    if sh.ix[row, "change_base"] > 0.03:
        close_base = sh.ix[row, "close"]
        sh.ix[row, "mark"] = mark_sell
        close_sell.append(row)
        close_sell.append(close_base)
        #print(close_sell)
    elif sh.ix[row, "change_base"] < -0.03:
        close_base = sh.ix[row, "close"]
        sh.ix[row, "mark"] = mark_buy
        close_buy.append(row)
        close_buy.append(close_base)
    else:
        sh.ix[row, "mark"] = mark_no_hanler

    #print(sh.ix[row, "change_base"], sh.ix[row, "mark"], sh.ix[row, "p_change"])



result = {"date": sh["date"], "open": sh["open"], "close": sh["close"],
          "change_base": sh["change_base"],"mark":sh["mark"]}
result = pd.DataFrame(result)

#print(result[:100])

#print(close_buy)

plt.plot(sh["close"], label="close")
close_sell_x = [x for x in close_sell if close_sell.index(x)%2 == 0]
close_sell_y = [y for y in close_sell if close_sell.index(y)%2 != 0]
close_buy_x = [x for x in close_buy if close_buy.index(x)%2 == 0]
close_buy_y = [y for y in close_buy if close_buy.index(y)%2 != 0]

"""
print(len(close_buy))
print(close_buy_x)
print(close_buy_y)
"""

plt.scatter(close_sell_x,close_sell_y, label="close_sell")
plt.scatter(close_buy_x,close_buy_y, label="close_buy")
plt.legend(loc="best")
plt.show()

