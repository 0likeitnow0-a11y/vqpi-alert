import yfinance as yf


def get_last_close(ticker):
    yf_ticker = yf.Ticker(f"{ticker}.SA")
    hist = yf_ticker.history(period="5d")

    if hist.empty:
        raise ValueError(f"Sem dados para {ticker}")

    return float(hist["Close"].iloc[-1])


def get_prices(tickers):
    prices = {}
    for t in tickers:
        prices[t] = round(get_last_close(t), 2)
    return prices
  
