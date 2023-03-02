#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:07:12 2022

@author: echellwig
"""

import pandas as pd #load pandas and call it pd
import matplotlib.pyplot as plt # load pyplot module of matplotlib
import matplotlib.ticker as tick


#set options so large numbers are not converted to scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#create data frame from csv
fn = "/Users/echellwig/Google Drive/Projects/IntroStats/data/raw_sales.csv"
sales = pd.read_csv(fn) 
sales = sales.loc[sales.propertyType=='house']

#some data manipulation
sales['postcode'] = sales['postcode'].astype(str)

sales['postcode'] =  '0' + sales['postcode']

sales['datesold'] = pd.to_datetime(sales['datesold'], format="%Y-%m-%d %H:%M:%S")

# Variable Creation
sales['Month'] = sales.datesold.dt.month
sales['Year'] = sales.datesold.dt.year



#line plot data
yr_sales = sales.loc[:, ['Year', 'price']].groupby('Year')
avg_price = yr_sales.median().reset_index()
sale_count = yr_sales.count().reset_index()
sale_count = sale_count.rename(columns={'price':'Sales'})

plt.plot(avg_price.Year, avg_price.price, color="#002E72")
plt.xlabel('Year')
plt.ylabel('House Price ($)')
plt.title('Average Housing Prices Over Time in RI')
plt.ylim([0, 800000], emit=False)
plt.show()

def ToThousands(x, pos):
    print(x)
    kn = round(float(x)/1000)
    kn_str = "{:,}".format(kn) + 'k'
    
    return kn_str


fig, ax = plt.subplots()
ax.plot(avg_price.Year, avg_price.price)
ax.set_title('Average Housing Prices Over Time in Rhode Island')
ax.set_ylabel('House Price ($)')
ax.set_xlabel('Year')
ax.set_ylim(ymin=0, ymax=12e5, emit=False)
ax.yaxis.set_major_formatter(tick.FuncFormatter(ToThousands))
#ax.yaxis.set_major_formatter(tick.FormatStrFormatter('%.2f'))
plt.show()

month_sales = sales.loc[:, ['Month', 'Year', 'price']].groupby('Month')
month_sales.count()
month_sales.mean()

def ToYear(x, pos):
    return pos + 2006


yr_list = [sales.loc[sales.Year==y].price for y in range(2007, 2020)]

fig3, ax3 = plt.subplots() #create subplot
ax3.boxplot(yr_list, showfliers=False)
ax3.set_title('Figure 3. Rhode Island Home Price Distributions by Year')
ax3.set_ylabel('House Price ($)', fontdict={'fontsize': 12}) #set x label
ax3.set_xlabel('Year', fontdict={'fontsize': 12}) #set y label
#ax3.xaxis.set_major_formatter(tick.FuncFormatter(ToYear))
ax.yaxis.set_major_formatter(tick.FuncFormatter(ToThousands))
plt.show()






