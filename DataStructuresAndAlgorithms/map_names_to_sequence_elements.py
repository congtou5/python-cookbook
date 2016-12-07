# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import namedtuple

# ***demo1***
Sub = namedtuple('Subscriber', ['addr', 'joined'])
print(Sub)  # <class '__main__.Subscriber'>
su = Sub('user@example.com', '2016-12-03')
print(su)  # Subscriber(addr='user@example.com', joined='2016-12-03')
print(su.addr)  # user@example.com
print(su.joined)  # 2016-12-03


# ***demo2***
# Using ordinary tuples
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# Using named tuples
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


print('-' * 15)

# ***demo3***
s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75 # AttributeError: can't set attribute
s = s._replace(shares=75)
print(s)
print('-' * 15)

# ***demo4***
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
