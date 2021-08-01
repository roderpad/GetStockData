import yfinance as yf

slack = yf.Ticker("WORK")

history = slack.history(period="max")

print(history)