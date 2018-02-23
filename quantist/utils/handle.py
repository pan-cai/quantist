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

class Handle(object):

    def handle_time(self):
        import pandas as pd
        import datetime
        import time

        data_path = "../quantist/data/pool/"
        stock_data = pd.read_excel(data_path + 'sh2.xls')
        stock_data['date'] = pd.to_datetime(stock_data['date'])
        demo_time = stock_data.ix[0, 'date']
        print(demo_time)  # 2017-12-22 00:00:00
        print(datetime.datetime.now())  # 2018-01-01 11:17:48.463440
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 2018-01-01 10:42:59
        print(demo_time.strftime("%Y-%m-%d %H:%M:%S"))  # 2017-12-22 00:00:00

        print((demo_time - datetime.datetime.now()).total_seconds())  # -902579.1432490001

        print(time.time())  # 1514775598.0781274
        print(datetime.datetime.now().date())  # 2018-01-01
        print(datetime.date.today() + datetime.timedelta(days=1))  # 2018-01-02
        print(datetime.date.today() - datetime.timedelta(days=3))  # 2017-12-29

        timestamp = time.mktime(demo_time.timetuple())
        print(timestamp)  # 1513872000.0
        print(datetime.datetime.fromtimestamp(timestamp))  # 2017-12-22 00:00:00
