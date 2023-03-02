#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:05:43 2022

@author: echellwig
"""


import pandas as pd #load pandas and call it pd

#set options so large numbers are not converted to scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#create data frame from csv
sales = pd.read_csv('data/raw_sales.csv') 

#some data manipulation
sales['postcode'] = sales['postcode'].astype(str)

sales['postcode'] =  '0' + sales['postcode']

sales['datesold'] = pd.to_datetime(sales['datesold'], format="%Y-%m-%d %H:%M:%S")

# Question 1
sales['Month'] = sales.datesold.dt.to_period('M')

# Question 7
price_ts = sales.loc[sales.postcode=='02615'].groupby(['Month'], as_index=False).price.mean()

price_ts = sales.loc[sales.postcode=='02615'].groupby(['Month'], as_index=False).price.mean()

price_ts['RollingAvg'] = price_ts.price.rolling(12).mean()

price_ts

price_ts.dropna(inplace=True)
