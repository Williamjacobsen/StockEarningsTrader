HOLD_STOCK_DAY_AMOUNT = 1
STOPLOSS = 4

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

class handle_dates():
    def two_digit_date(self, num):
        """Input: '7', Output: '07'"""

        if len(str((num))) < 2:
            return "0" + str(num)
        return num

    def convert_date(self, date):
        """Input: 'Jul 27, 2021', Output: '2021-7-27'"""

        date = date.replace(",", "")
        year = self.two_digit_date(date[-4:])
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = self.two_digit_date(months.index(date[:3]))
        day = self.two_digit_date(date[4:6])
        return str(year) + '-' + str(month) + '-' + str(day)

    def is_leap_year(self, year):
        return year % 4 == 0

    def add_days_to_date(self, date, add_days = 0):
        """adds days to date (only within a month)"""

        days = int(date.split('-')[2])
        month = int(date.split('-')[1])
        year = int(date.split('-')[0])

        month_days = {
            "01": 31,
            "02": 29 if self.is_leap_year(year) else 28,
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

        new_days = days + add_days
        days_in_month = month_days[self.two_digit_date(date.split('-')[1])]

        if new_days > days_in_month:
            return f"{year}-{self.two_digit_date(month + 1)}-{self.two_digit_date(new_days - days_in_month)}"

        elif 0 > new_days:
            return f"{year}-{self.two_digit_date(month - 1)}-{(month_days[self.two_digit_date(month - 1)]) - (-add_days - days)}"

        return f"{year}-{self.two_digit_date(month)}-{self.two_digit_date(new_days)}"

class handle_json():
    def save_results(self, symbol, result):
        with open("results.json", "r") as f:
            data = json.loads(f.read())
            data[symbol] = result
            f.close()

        with open("results.json", "w") as f:
            json.dump(data, f, indent=4)
            f.close()
    
    def read_earning_dates(self):
        with open("stock_earnings.json", "r") as f:
            stock_earnings = json.loads(f.read())
            f.close()
        return stock_earnings

class analysis_utilities():
    def __init__(self, stock):
        self.stock = stock

    def stock_close_change_dates(self, start_date, end_date):
        """Gets change (%) of stock change between close of start_date and close of end_date"""
        return (float(self.stock.loc[[end_date]]['Close']) - float(self.stock.loc[[start_date]]['Close'])) / float(self.stock.loc[[start_date]]['Close']) * 100

    def calculate_current_procent_price(self, start_date):
        return float(self.stock.loc[[start_date]]['Close']) / 100
    
    def stop_loss(self, start_date, end_date):
        cur_date = handle_dates().add_days_to_date(start_date, 0)

        start_price = float(self.stock.loc[[start_date]]['Close'])
        stop_loss_value = start_price - (self.calculate_current_procent_price(start_date) * STOPLOSS)

        while cur_date != end_date:
            cur_date = handle_dates().add_days_to_date(cur_date, 1)
            low = float(self.stock.loc[[cur_date]]['Low'])

            if low < stop_loss_value:
                return -STOPLOSS
        return False

def backtest_strategy():
    earnings_data = handle_json().read_earning_dates()
    
    for symbol in earnings_data:
        stock = yf.download(tickers = symbol, period = "3y", interval = "1d", prepost = False, repair = True)
        
        total_stock_result = 0.00
        trades = []

        for date in earnings_data[symbol]:
            date = handle_dates().convert_date(date)

            #start_date = handle_dates().add_days_to_date(date, 0)
            #end_date = handle_dates().add_days_to_date(date, HOLD_STOCK_DAY_AMOUNT + 1)
            start_date = handle_dates().add_days_to_date(date, -1)
            end_date = handle_dates().add_days_to_date(date, HOLD_STOCK_DAY_AMOUNT)

            try:
                stop_loss = analysis_utilities(stock).stop_loss(start_date, end_date)
                if stop_loss != False:
                    total_stock_result += stop_loss
                    trades.append(stop_loss)
                    print("date: " + date + " - stop loss: " + str(stop_loss))
                    continue
            except Exception as e:
                pass

            try:
                result = analysis_utilities(stock).stock_close_change_dates(start_date, end_date)
                total_stock_result += result
                trades.append(result)
                print("date: " + date + " - result: " + str(result))
            except Exception as e:
                pass
        
        handle_json().save_results(symbol, {"result": total_stock_result, "trades": trades})
        print(symbol + ": " + str(total_stock_result))

if __name__ == '__main__':
    backtest_strategy()