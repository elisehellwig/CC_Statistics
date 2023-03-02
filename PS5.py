#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:57:00 2023

@author: echellwig
"""

import pandas as pd #load pandas and call it pd
import matplotlib.pyplot as plt # load pyplot module of matplotlib 
import matplotlib.ticker as tck # load the ticker module of matplotlib

yrs = range(2007, 2020) # years in dataset

#set options so large numbers are not converted to scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x) # Question 1 

#Load in data from csv
sales = pd.read_csv('data/raw_sales.csv')

#only include 3-bedroom houses so we are comparing apples to apples
sales = sales.loc[sales.propertyType=='house'] 
sales = sales.loc[sales.bedrooms==3]

#Converting datestring to datetime class
sales['datesold'] = pd.to_datetime(sales['datesold'], format="%Y-%m-%d %H:%M:%S")

# Extracting year from datetime class
sales['Year'] = sales.datesold.dt.year

#Price by year
yr_sales = sales.loc[:, ['Year', 'price']].groupby('Year') 

avg_price = yr_sales.mean().reset_index() # Question 2 

median_price = yr_sales.median().reset_index()

#Question 3
yr_list = [sales.loc[sales.Year==y].price for y in yrs]

#Question 4
plt.plot(median_price.Year, median_price.price) #create plot 
plt.show() #display plot

pt12 = {'fontsize': 12}

# Question 5
line_title = ' Median Rhode Island Home Prices, 2007-2019\n ' 
subtitle = 'Single Family 3-bedroom'

########Figure 1##############
plt.plot(median_price.Year, median_price.price, color='#002E72', marker='o') 
plt.ylim(ymin=0, ymax=6e5)
plt.title("Figure 1." + line_title + subtitle, loc='left', fontdict=pt12) 
plt.xlabel('Year')
plt.ylabel('House Price ($)')
plt.show()



#############figure 2############
def ToThousands(x, pos): #function to convert number to thousands
    kn = round(x/1000) # divide by 1000 and turn into an integer
    kn_str = "{:,}".format(kn) + 'k' #add a k on the end to denote thousands
    return kn_str

fig2, ax2 = plt.subplots() #Question 6, create objects to use to create our line plot 
ax2.plot(median_price.Year, median_price.price, color='#002E72') # add line data to plot 
ax2.set_title('Figure 2.' + line_title + subtitle, loc='left', fontdict=pt12) #title 
ax2.set_ylabel('House Price ($)', fontdict=pt12) #set x label
ax2.set_xlabel('Year', fontdict=pt12) #set y label 
ax2.set_ylim(ymin=0, ymax=6e5) #start y axis at 0
ax2.yaxis.set_major_formatter(tck.FuncFormatter(ToThousands)) #Question 8 
plt.show()


################# Figure 3#################

box_title = " Rhode Island Home Price Distributions, 2007-2019\n "
fig3, ax3 = plt.subplots() #create figure and subplot 
ax3.boxplot(yr_list) #add boxplot to figure
ax3.set_ylim(ymin=0) #set y minimum to 0
ax3.set_title('Figure 3.' + box_title + subtitle, #Add title
loc='left', fontdict=pt12) # set title location and size
ax3.set_ylabel('House Price ($)', fontdict=pt12) #set x label, and size 
ax3.set_xlabel('Year', fontdict=pt12) #set y label and size
plt.show()


orange = dict(color='#E07102', linewidth=2)

def ToYear0(x, pos): #turn x value for boxplot into year
    return x + 2006


#######################Figure 4#######################
fig4, ax4 = plt.subplots() #create subplot
# add boxplot to figure without outliers
ax4.boxplot(yr_list, showfliers=False, medianprops=orange, notch=True, 
            bootstrap=int(1e4))
ax4.set_ylim(ymin=0)
ax4.set_title('Figure 4.' + box_title + subtitle, loc='left', fontdict=pt12)
ax4.set_ylabel('House Price ($)', fontdict=pt12) #set y label 
ax4.set_xlabel('Year', fontdict=pt12) #set x label 
ax4.xaxis.set_major_formatter(tck.FuncFormatter(ToYear0)) #format x axis 
ax4.yaxis.set_major_formatter(tck.FuncFormatter(ToThousands)) # format y axis 
ax4.tick_params(axis='x', labelrotation = 45) #rotate x axis labels 
plt.show()



