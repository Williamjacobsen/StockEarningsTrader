import json

import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def stock_win_rate(results):
    wins = 0
    lost = 0
    for symbol in results:
        if results[symbol]["result"] > 0:
            wins += 1
        elif results[symbol]["result"] < 0:
            lost += 1
    return round(wins / (wins + lost) * 100, 2), wins + lost, wins, lost

def total_win_rate(results):
    wins = 0
    lost = 0
    for symbol in results:
        for trade in results[symbol]["trades"]:
            if trade > 0:
                wins += 1
            elif trade < 0:
                lost += 1
    return round(wins / (wins + lost) * 100, 2), wins + lost, wins, lost

def profit(results):
    _profit = 0
    for symbol in results:
        _profit += results[symbol]["result"]
    return round(_profit, 2)

def analysis(logging=True):
    with open("results.json", "r") as f:
        results = json.loads(f.read())
        _stock_win_rate, stock_trades, stock_wins, stock_lost = stock_win_rate(results)
        _total_win_rate, total_trades, total_wins, total_lost = total_win_rate(results)
        _profit = profit(results)

        f.close()

    if logging:
        print(f"stock_win_rate: {_stock_win_rate}%")
        print(f"stock_trades: {stock_trades}")
        print(f"stock_wins: {stock_wins}")
        print(f"stock_lost: {stock_lost}")
        print("")
        print(f"total_win_rate: {_total_win_rate}%")
        print(f"total_trades: {total_trades}")
        print(f"total_wins: {total_wins}")
        print(f"total_lost: {total_lost}")
        print("")
        print(f"profit: {_profit}%")

def optimize_settings():
    pass

if __name__ == '__main__':
    analysis(logging=False)
