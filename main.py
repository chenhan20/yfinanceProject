import yfinance as yf


ticker = "TSLA"
msft = yf.Ticker(ticker)

# get stock info
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = (data.tail(1)['Close'].iloc[0])
print(data.tail(1)['Close'])
print(ticker,last_quote)