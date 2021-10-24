import yfinance as yf


ticker = "TSLA"

msft = yf.Ticker(ticker)
stock_info = yf.Ticker(ticker).info

# get stock info
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = (data.tail(1)['Close'].iloc[0])

# market_price = stock_info['regularMarketPrice']
# previous_close_price = stock_info['regularMarketPreviousClose']
# print('market price ', market_price)
# print('previous close price ', previous_close_price)

print('Date:',str(data.tail(1)['Close'].index.values[0]))
print(ticker,last_quote)