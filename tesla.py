import pandas as pd

import yfinance as yf

tesla = yf.Ticker("TSLA")
tesla_data = tesla.data



for key, value in tesla_info.items():
    print(key, ":", value)

print(tesla_data['country'])
print(tesla_data['sector'])
tesla_share_price_data = tesla.history(period="max")

print(tesla_share_price_data)

print((tesla_share_price_data.reset_index(inplace=True))

