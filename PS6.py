#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:21:14 2023

@author: echellwig
"""

import pandas as pd #load pandas and call it pd
import matplotlib.pyplot as plt # load pyplot module of matplotlib
import matplotlib.ticker as tck # load the ticker module of matplotlib
import numpy.random as rand #load random module of numpy and call it rand


yrs = range(2007, 2020) # years in dataset

#set options so large numbers are not converted to scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x) # Question 1

#Load in data from csv
sales = pd.read_csv('data/raw_sales.csv') 
#Converting datestring to datetime class
sales['datesold'] = pd.to_datetime(sales['datesold'], format="%Y-%m-%d %H:%M:%S")

# Extracting year from datetime class
sales['Year'] = sales.datesold.dt.year


rand.seed(5)

a = rand.choice(range(50),50)
b = rand.choice(range(50),50)

x = rand.uniform(-10, 10, 50)
y = rand.uniform(0, 6, 50)


Ax = a*0.85 + x
Ay =  a*-0.25 + y
Bx = b*-.4 + x
By = b*0.6 + y


df = pd.DataFrame({'A':a, 'B':b, 'Ax': Ax, 'Ay':Ay, 'Bx':Bx, 'By':By})

# plt.scatter(df.A, df.Ax)
# plt.show()


fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

ax[0,0].scatter(df.A, df.Ax, s=8)
ax[0,1].scatter(df.A, df.Ay, s=8)
ax[1,0].scatter(df.B, df.Bx, s=8)
ax[1,1].scatter(df.B, df.By, s=8)

fig.suptitle('Figure X. Displaying some randomly generated data', fontsize=16)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#         ylim=(0, 8), yticks=np.arange(1, 8))

plt.subplots_adjust(wspace=0, hspace=0)

plt.show()