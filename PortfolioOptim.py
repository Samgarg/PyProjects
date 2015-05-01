__author__ = 'Davidws'

import pandas as pd
from pandas.io.data import DataReader as dr
from datetime import datetime
import numpy as np
from numpy.linalg import inv

symbols = ['ORCL','MSFT','AAPL'] #Define the tickers we want in our project
start_date = '2010-01-01' # Give the start of the date range
d = {} # Create an empty dictionary to hold them
for ticker in symbols:
    d[ticker] = dr(ticker, 'yahoo',start_date) # Iterate over the tickers and get the stock data into our dictionary
pan = pd.Panel(d) # Create a Panel of the Data - this will allow us to Melt / Cast
close = pan.minor_xs('Adj Close') # Cast on the Adj Close - We could use any of the available columns here
# Careful about the tickers - some stocks are not this old and wont have data then we need to determine what to do about the NAN as we calculate the covariance.

count_tickers = symbols.__len__() # Get the Number of Stock Tickers we want

exp_return = close.mean(0) # Calculate the E(R) for the stocks
sd_stock = close.std # Calculate the Std.Dev for the stocks
cov_stock = close.cov() # Calculate the Covariance Matrix for the stocks
# Uncomment below if you want to write this to a file - add your own path
# path = ('C:/...)
# close.to_csv(path + 'close.csv', sep=',')
inv_cov = inv(cov_stock) # Calculates the inverse of the covariance matrix - This may be going too far for our solution so far.