# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# In order to perform useful calculations on the dictionary contents,
# invert the keys and values of the dictionary using zip()
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
print('-' * 15)

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
#print(max(prices_and_names))  # ValueError:max() arg is an empty sequence
print('-'*15)

print(min(prices)) # AAPL
print(max(prices)) # IBM
print(min(prices.values())) # 10.75
print(max(prices.values())) # 612.78
print(min(prices, key=lambda k:prices[k])) # FB
print(max(prices, key=lambda k:prices[k])) # AAPL