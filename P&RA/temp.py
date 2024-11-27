import dateutil.utils
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from main import *
from scipy.stats import norm


def get_data(symbol, start, end) -> plt:
    data = pd.DataFrame(yf.download(tickers=symbol, start=start, end=end)['Adj Close'])
    plt.plot(data)
    plt.tick_params(axis='x', labelrotation=45)
    plt.xticks(fontsize='x-small')
    plt.show()


get_data('NVDA', dt.date.today() - dt.timedelta(365), dt.date.today())
