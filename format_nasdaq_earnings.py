import json

with open("nasdaq_earnings.json", "r") as f:
    stock_earnings = json.loads(f.read())
    f.close()

for idx, i in enumerate(stock_earnings):
    for jdx, j in enumerate( i):
        if "." in j["symbol"]:
            stock_earnings[idx][jdx]["symbol"] = i[jdx]["symbol"].replace(".", "-")


with open("nasdaq_earnings.json", "w") as f:
    json.dump(stock_earnings, f, indent=4)
    f.close()