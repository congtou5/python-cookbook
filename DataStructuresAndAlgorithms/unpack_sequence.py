# ！/usr/bin/env python3
# -*- coding:utf-8 -*-

# demo1
p = (4, 5)
x, y = p
print(x)
print(y)
print('-----------')

# demo2
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, month, day) = data
print(name)
print(shares)
print(price)
print(year)
print(month)
print(day)
print('-----------')

# unpacking works with any object that happens to be iterable, including:tuples,lists
# stings, files, iterators, and generators

# demo3
_, shares, price, _ = data
print(shares)
print(price)


