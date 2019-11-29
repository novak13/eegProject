import pandas as pd
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
import matplotlib
from datetime import datetime


# Pulling info from the iexfinance API
def getCompanyInfo(symbols):
    current_stock = Stock(symbols, token=IEX_TOKEN)
    company_info = current_stock.get_company()
    return company_info

def getEarnings(symbols):
    stock_batch = Stock(symbols, token=IEX_TOKEN)
    earnings = stock_batch.get_earnings()
    return earnings

def getHistoricalPrices(stock):
    return get_historical_data(stock, start, end, output_format='pandas', token=IEX_TOKEN)

#Global iexfinance variable for the token
# IEX_TOKEN = 'AgEIcHlwaS5vcmcCJGYxNTA2ZmJiLWFmNGQtNDEwYS1hMjgyLWMzMWY1ZTY2YmE5YwACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgOFxZsMFOcQ1ANMJxldPS7t4ZYInBINWi8tOw07nm3-0'
#IEX_TOKEN = 'sk_ed6c26c93afd4eebb6013958a8546486'
IEX_TOKEN='pk_a9eefc73bcf345b0b6adde61855b1c42'

# Get list of current S&P companies
table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])

# Pull that list into a dataframe
sp = pd.read_csv('S&P500-Symbols.csv', index_col=[0])

sp_company_info = getCompanyInfo(sp["Symbol"][:5].tolist())

company_info_to_df = []
for company in sp_company_info:
    company_info_to_df.append(sp_company_info[company])

columns = ['symbol', 'companyName', 'exchange', 'industry', 'website', 'CEO', 'sector']
df = pd.DataFrame(company_info_to_df, columns=columns)
df.head()


single_stock_earnings = getEarnings(df)
df_earnings = pd.DataFrame(single_stock_earnings)
df_earnings.head()

#     start = datetime(2016, 1, 1)
#     end = datetime(2019, 11, 23)
#     single_stock_history = getHistoricalPrices(i)
#
#     # Graph the data
#     single_stock_history['close'].plot(label="3M Close")
