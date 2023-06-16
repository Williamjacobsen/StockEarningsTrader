import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

import yfinance as yf
import pandas as pd
import json

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def two_digit_date(num):
    if len(str((num))) < 2:
        return "0" + str(num)
    return num

def convert_date(date):
    date = date.replace(",", "")
    year = two_digit_date(date[-4:])
    months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = two_digit_date(months.index(date[:3]))
    day = two_digit_date(date[4:6])
    return str(year) + '-' + str(month) + '-' + str(day)

def is_leap_year(year):
    return year % 4 == 0


def add_days_to_date(date, days = 0):
    """adds days to date (only within a month)"""

    month_days = {
        "01": 31,
        "02": 29 if is_leap_year(int(date.split('-')[0])) else 28,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31
    }

    if int(date.split('-')[2]) + days > month_days[str(date.split('-')[1])]:
        return f"{date.split('-')[0]}-{two_digit_date(int(date.split('-')[1]) + 1)}-{two_digit_date(int(date.split('-')[2]) + days - month_days[str(date.split('-')[1])])}"

    elif int(date.split('-')[2]) + days < 0:
        return f"{date.split('-')[0]}-{two_digit_date(int(date.split('-')[1]) - 1)}-{(month_days[str(two_digit_date(int(date.split('-')[1]) - 1))]) - (-days - int(date.split('-')[2]))}"

    date = f"{date.split('-')[0]}-{two_digit_date(date.split('-')[1])}-{two_digit_date(int(date.split('-')[2]) + days)}"

    return date

def stock_close_change_dates(stock, start_date, end_date):
    """Gets change (%) of stock change between close of start_date and close of end_date"""
    return (float(stock.loc[[end_date]]['Close']) - float(stock.loc[[start_date]]['Close'])) / float(stock.loc[[start_date]]['Close']) * 100

def calculate_current_procent_price(stock, date):
    return float(stock.loc[[date]]['Close']) / 100

def stop_loss(position, stock, start_date, end_date):
    if position == "long":
        pass # go through each day see if low is lower than one procent

def save_results(symbol, result):
    with open("results.json", "r") as f:
        data = json.loads(f.read()) 
        data[symbol] = result
        f.close()

    with open("results.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()

if __name__ == '__main__':
    #stock = yf.download(tickers = "CCEP", period = "3y", interval = "1d", prepost = False, repair = True)
    #stock = stock.reset_index()

    #total_profit = 0.00

    profits = {}

    with open("stock_earnings.json", "r") as f:
        stock_earnings = json.loads(f.read())
        f.close()

    for symbol in stock_earnings:
        total_profit = 0.00

        stock = yf.download(tickers = symbol, period = "3y", interval = "1d", prepost = False, repair = True)

        dates = stock_earnings[symbol]
        #dates = []
        for date in dates:
            date = convert_date(date)
            #date = convert_date("Mar 04, 2021")

            try:
                profit = stock_close_change_dates(stock, add_days_to_date(date=date, days=-1), add_days_to_date(date=date, days=1))
                total_profit += profit
                #print("profit: " + str(profit))
            except Exception:
                pass
        profits[symbol] = total_profit
        save_results(symbol, total_profit)
        print(symbol + ": " + str(profits[symbol]))

    #print("total profit: " + str(total_profit))
    



