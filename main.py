import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def calculate_statistics(data):
    mean_price = data['Close'].mean()
    volatility = data['Close'].std()
    return mean_price, volatility

def plot_stock_data(data, ticker):
    data['Close'].plot(title=f"Ціна акцій {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("Ціна закриття")
    plt.show()

def main():
    ticker = input("Введіть тікер акцій (наприклад, 'AAPL' для Apple): ")
    start_date = input("Введіть дату початку у форматі РРРР-ММ-ДД (наприклад, '2020-01-01'): ")
    end_date = input("Введіть дату кінця у форматі РРРР-ММ-ДД (наприклад, '2021-01-01'): ")

    stock_data = download_stock_data(ticker, start_date, end_date)

    mean_price, volatility = calculate_statistics(stock_data)
    print(f"Середня ціна: {mean_price}, Волатильність: {volatility}")

    plot_stock_data(stock_data, ticker)

if __name__ == "__main__":
    main()
