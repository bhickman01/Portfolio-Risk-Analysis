import dateutil.utils
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from main import *
from scipy.stats import norm

# 1. Implement various VaR methods(historical, monte carlo, variance-covariance)
# 2. Calculate portfolio Beta
# 3. Calculate portfolio volatility

years = 15
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365 * years)

startDate.strftime('%Y-%m-%d')
endDate.strftime('%Y-%m-%d')

tickers = []

for ticker in p1.portfolio:
    tickers.append(ticker)


def historical_var(symbols, days, confidence_interval, value):
    adj_close_df = pd.DataFrame(yf.download(tickers=symbols, start=startDate, end=endDate)['Adj Close'])

    log_returns = np.log(adj_close_df / adj_close_df.shift(1))  # a given days price / the previous days and taking the log
    log_returns = log_returns.dropna()

    # Creating an Equally Weighted Portfolio
    weights = np.array([1 / len(symbols)] * len(symbols))  # we are adding weights so that everything has the same risk

    historical_returns = (log_returns * weights).sum(axis=1)  # applying the weights to the log returns from before
    range_returns = historical_returns.rolling(window=days).sum()
    range_returns = range_returns.dropna()

    var = -np.percentile(range_returns,
                         100 - (confidence_interval * 100)) * value  # The VaR for a 95% confidence
    # interval. This would tell us how must loss we would accrue in the 5th percentile
    return var


def parametric_var(symbols, days, confidence_interval, value):
    adj_close_df = pd.DataFrame(yf.download(tickers=symbols, start=startDate, end=endDate)['Adj Close'])

    log_returns = np.log(adj_close_df / adj_close_df.shift(1)).dropna()

    weights = np.array([1/len(symbols)] * len(symbols))

    # Create covariance matrix
    cov_matrix = log_returns.cov() * 252 # number of trading days in the US per year

    # Create portfolio standard deviation
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    var = value * (norm.ppf(confidence_interval) * portfolio_std_dev * np.sqrt(days / 252))

    # ^ norm.ppf(confidence_interval) would give us the z-score
    return var

# print(f"Historical VaR at {0.95 * 100}%: ${historical_var(tickers, 10, 0.95, portfolio_value)}")
# print(f"Parametric VaR at {0.95 * 100}%: ${parametric_var(tickers, 10, 0.95, portfolio_value)}")

def historical_data(symbol, start, end) -> plt:
    data = pd.DataFrame(yf.download(tickers=symbol, start=start, end=end)['Adj Close'])
    plt.plot(data)
    plt.tick_params(axis='x', labelrotation=45)
    plt.xticks(fontsize='x-small')
    plt.show()


AAPL = historical_data('AAPL', dt.date.today() - dt.timedelta(365), dt.date.today())
MSFT = historical_data('MSFT', dt.date.today() - dt.timedelta(365), dt.date.today())









