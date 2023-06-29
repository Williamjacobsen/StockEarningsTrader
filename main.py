import os
import yfinance as yf
import json
import datetime

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class handle_dates():
    def two_digit_date(self, num):
        """Input: '7', Output: '07'"""

        if len(str((num))) < 2:
            return "0" + str(num)
        return str(num)

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

        while add_days != 0:

            if add_days < 0:
                days -= 1
            else:
                days += 1

            if days > month_days[self.two_digit_date(month)]:
                if month != 12:
                    month += 1
                else:
                    month = 1
                    year += 1
                days = 1
            elif days < 1:
                if month != 1:
                    month -= 1
                else:
                    month = 12
                    year -= 1
                days = month_days[self.two_digit_date(month)]
            
            if datetime.datetime(year, month, days).weekday() < 4:
                if add_days > 0:
                    add_days -= 1
                else:
                    add_days += 1

        return f"{year}-{self.two_digit_date(month)}-{self.two_digit_date(days)}"

class handle_json():
    def save_results(self, symbol, result):
        with open("results.json", "r") as f:
            data = json.loads(f.read())
            try:
                data[symbol]["trades"].append(result["trades"][0])
                data[symbol]["result"] = data[symbol]["result"] + result["result"]
            except Exception:
                data[symbol] = result
            f.close()

        with open("results.json", "w") as f:
            json.dump(data, f, indent=4)
            f.close()
    
    #def read_earning_dates(self):
    #    with open("stock_earnings.json", "r") as f:
    #        stock_earnings = json.loads(f.read())
    #        f.close()
    #    return stock_earnings

    def read_earning_dates(self):
        with open("nasdaq_earnings.json", "r") as f:
            stock_earnings = json.loads(f.read())
            f.close()
        return stock_earnings

class analysis_utilities():
    def __init__(self, stock):
        self.stock = stock

    def stock_change_dates(self, start_stick, end_stick, start_date, end_date):
        """Gets change (%) of stock change between start_stick of start_date and end_stick of end_date"""
        return (float(self.stock.loc[[end_date]][end_stick]) - float(self.stock.loc[[start_date]][start_stick])) / float(self.stock.loc[[start_date]][start_stick]) * 100

    def calculate_current_procent_price(self, stick, start_date):
        return float(self.stock.loc[[start_date]][stick]) / 100
    
    def stop_loss(self, position, stick, start_date, end_date):
        cur_date = start_date

        start_price = float(self.stock.loc[[start_date]][stick])
        stop_loss_value = start_price - ((start_price / 100) * STOPLOSS) if position == "long" else start_price + ((start_price / 100) * STOPLOSS)

        while cur_date != handle_dates().add_days_to_date(end_date, 1):
            low = float(self.stock.loc[[cur_date]]['Low'])
            high = float(self.stock.loc[[cur_date]]['High'])
            _open = float(self.stock.loc[[cur_date]]['Open'])
            
            if position == "long":
                if low < stop_loss_value:
                    if _open < stop_loss_value:
                        return self.stock_change_dates('Open', 'Open', start_date, cur_date)
                    return -STOPLOSS
            elif position == "short":
                if high > stop_loss_value:
                    if _open > stop_loss_value:
                        return -self.stock_change_dates('Open', 'Open', start_date, cur_date)
                    return -STOPLOSS
            
            cur_date = handle_dates().add_days_to_date(cur_date, 1)

        return False

def settings():
    with open('settings.json') as f:
        _settings = json.loads(f.read())
        f.close()
    return _settings["HOLD_STOCK_DAY_AMOUNT"], _settings["STOPLOSS"], _settings["LOGGING"]

def backtest_strategy_buy_on_open():
    earnings_data = handle_json().read_earning_dates()

    paper_money = 1000

    for data in earnings_data:

        _len = 0
        for _list in data:
            date = _list['date']
            marketCap = _list['marketCap']
            
            if marketCap == "":
                continue
            
            if int(marketCap[1:].replace(",", "")) > 1000000000:
                _len += 1

        for _list in data:
            date = _list['date']
            symbol = _list['symbol']
            marketCap = _list['marketCap']

            #if date == in_trade_date or date == handle_dates().add_days_to_date(in_trade_date, -1):
            #    continue
            
            if marketCap == "":
                continue

            if int(marketCap[1:].replace(",", "")) > 1000000000:
                stock = yf.download(tickers=symbol, start=handle_dates().add_days_to_date(date, -5), end=handle_dates().add_days_to_date(date, 5), interval="1d", prepost=False, repair=True, threads=True, progress=False)

                total_stock_result = 0.00
                trades = []

                start_date = date # open
                end_date = handle_dates().add_days_to_date(date, HOLD_STOCK_DAY_AMOUNT) # close
                
                try:
                    result = analysis_utilities(stock).stock_change_dates('Open', 'Close', start_date, end_date)
                    total_stock_result += result
                    trades.append(result)
                    print("symbol: " + symbol + " - date: " + date + " - result: " + str(result)) if LOGGING else None

                    handle_json().save_results(symbol, {"result": total_stock_result, "trades": trades})
                    #print(symbol + ": " + str(total_stock_result)) if LOGGING else None
                    
                    paper_money += ((paper_money / _len) / 100) * total_stock_result
                    print("paper_money: " + str(paper_money))
                except Exception as e:
                    pass
    
if __name__ == '__main__':
    HOLD_STOCK_DAY_AMOUNT, STOPLOSS, LOGGING = settings()

    if LOGGING:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    backtest_strategy_buy_on_open()