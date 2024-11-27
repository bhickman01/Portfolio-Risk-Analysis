import datetime as dt
import yfinance as yf


class Portfolio:

    def __init__(self, name):
        self.name = name
        self.portfolio = {}

    def add_stock(self, ticker, date, price, quantity):
        if ticker not in self.portfolio:
            self.portfolio[ticker] = {}

        if date in self.portfolio[ticker]:
            self.portfolio[ticker][date]['quantity'] += quantity
        else:
            self.portfolio[ticker][date] = {'date': date, 'price': price, 'quantity': quantity}

    def remove_stock(self, ticker):
        if ticker:
            self.portfolio.pop(ticker)
        else:
            print("Stock does not exist in portfolio")

    def display_stocks(self):
        for ticker in self.portfolio.items():
            return ticker


    def calc_portfolio_value(self, current_prices):
        total = 0
        for ticker, transaction in self.portfolio.items():
            for price, details in transaction.items():
                current_price = current_prices.get(ticker, details['price'])
                total += details['quantity'] * current_price
        return total

    def fetch_current_prices(self):
        tickers = list(self.portfolio.keys())
        current_prices = {}
        data = yf.download(tickers=tickers, period='1d')['Adj Close'].iloc[-1]
        for ticker in tickers:
            current_prices[ticker] = data[ticker]
        return current_prices
