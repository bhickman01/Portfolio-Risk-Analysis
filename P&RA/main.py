from portfolio import Portfolio
import yfinance as yf
import datetime as dt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p1 = Portfolio("My Portfolio")

p1.add_stock('MSFT', '2024-04-30', 398, 2)
p1.add_stock('ORCL', '2024-08-01', 139, 1)
p1.add_stock('AAPL', '2023-10-23', 177, 2)

# Get all the current prices for the stocks we have in the portfolio
current_prices = p1.fetch_current_prices()

# Get the current value of the portfolio given market conditions (portfolio value is the current stock price * quantity)
portfolio_value = p1.calc_portfolio_value(current_prices)

years = 15
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365 * years)

root = tk.Tk()
root.title("Portfolio Optimisation & Risk Management Tool 1.1")
root.geometry("1000x600")

label = tk.Label(root, text="Enter ticker name")
label.pack()

entry = tk.Entry(root)
entry.pack()

stock_data_frame = tk.Frame(root, width=800, height=400)
stock_data_frame.pack(padx=10, pady=10)
stock_data_frame.pack_propagate(False)

def show_portfolio():
    my_stocks = "\n".join(f"{stock}" for stock in p1.display_stocks())
    dict_label.config(text=my_stocks)


# retrieves the historical data to be used in the display
def stock_data(symbol, start, end) -> plt:
    data = pd.DataFrame(yf.download(tickers=symbol, start=start, end=end)['Adj Close'])
    fig, ax = plt.subplots()
    ax.plot(data)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_xlabel("Date")
    ax.set_ylabel("Adjust Close Price (USD)")
    return fig

# displays the stock data
def display_stock():
    stock_ticker = entry.get()
    data = stock_data(stock_ticker, startDate, endDate)

    for widget in stock_data_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(data, master=stock_data_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# on click, the button loads the stock data graph into the frame
button = tk.Button(root, text="Show Graph", command=display_stock)
button.pack(pady=10)

dict_label = tk.Label(root, text="", justify="left", anchor="w")
dict_label.pack()

portfolio_stocks = tk.Button(root, text="Portfolio Stocks", command=show_portfolio)
portfolio_stocks.pack()

root.mainloop()
