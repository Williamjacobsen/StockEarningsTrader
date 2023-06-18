import json

def win_rate(results):
    wins = 0
    trades = 0
    for result in results:
        if results[result] > 0:
            wins += 1
        trades += 1
    return wins/trades * 100, wins, trades - wins

def calculate_profit(results):
    profit = 0
    for result in results:
        profit += results[result]
    return profit

if __name__ == '__main__':
    with open("results.json", "r") as f:
        results = json.loads(f.read())
        _win_rate, wins, lost = win_rate(results)
        profit = calculate_profit(results)
        f.close()
    
    print(f"Win Rate (%): {_win_rate}")
    print(f"Wins: {wins}")
    print(f"Lost: {lost}")
    print(f"Total stocks traded: {wins + lost}")
    print(f"Profit (%): {profit}")