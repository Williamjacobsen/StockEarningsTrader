import json
import os
import time

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
        print(f"profit per trade: {round(_profit/total_trades, 2)}%")
    return {
        "stock_win_rate": _stock_win_rate, 
        "stock_trades": stock_trades, 
        "stock_wins": stock_wins, 
        "stock_lost": stock_lost,
        "total_win_rate": _total_win_rate,
        "total_trades": total_trades,
        "total_wins": total_wins,
        "total_lost": total_lost,
        "profit": _profit,
        "profit per trade": round(_profit/total_trades, 2)
    }

def save_settings_result(result, stoploss, hold_stock_day_amount):
    with open("settings_result.json", "r") as f:
        data = json.loads(f.read())
        data["Buy on open of earnings report"][f"'STOPLOSS': {stoploss}, 'HOLD_STOCK_DAY_AMOUNT': {hold_stock_day_amount}"] = result
        f.close()

    with open("settings_result.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()

def change_settings(stoploss, hold_stock_day_amount):
    with open("settings.json", "r") as f:
        data = json.loads(f.read())
        data["STOPLOSS"] = stoploss
        data["HOLD_STOCK_DAY_AMOUNT"] = hold_stock_day_amount
        f.close()

    with open("settings.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()

def optimize_settings():
    hold_stock_day_amount = 1
    #for stoploss in range(1, 6):
    #    stoploss = stoploss / 10
    #    change_settings(stoploss, hold_stock_day_amount)
    #    time.sleep(1)
    #    print(f"running [STOPLOSS: {stoploss}] & [HOLD_STOCK_DAY_AMOUNT: {hold_stock_day_amount}]")
    #    os.system('python main.py')
    #    time.sleep(1)
    #    result = analysis(False)
    #    time.sleep(1)
    #    save_settings_result(result, stoploss, hold_stock_day_amount)
    for stoploss in range(1, 7):
        if stoploss == 6:
            stoploss = 100
        change_settings(stoploss, hold_stock_day_amount)
        time.sleep(1)
        print(f"running [STOPLOSS: {stoploss}] & [HOLD_STOCK_DAY_AMOUNT: {hold_stock_day_amount}]")
        os.system('python main.py')
        time.sleep(1)
        result = analysis(False)
        time.sleep(1)
        save_settings_result(result, stoploss, hold_stock_day_amount)


if __name__ == '__main__':
    optimize_settings()
