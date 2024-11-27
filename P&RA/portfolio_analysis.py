import pandas as pd
import numpy as np
import yfinance as yf
from main import *


# 1. Implement Mean-Variance Optimisation
# 2. Implement Equal Weight Portfolio
# 3. Implement portfolio performance metrics (annualised and cumulative returns, alpha, Sortino and Treynor ratio)

def equal_weight(symbols):
    return np.array([1 / len(symbols)] * len(symbols))




