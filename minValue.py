stock = {'GOOG': 434,
        'AAPL': 325,
        'FB' : 54,
        'AMZN' : 623,
        'MSFT' : 549}

min_price = min(zip(stock.values(), stock.keys()))
print(min_price)
