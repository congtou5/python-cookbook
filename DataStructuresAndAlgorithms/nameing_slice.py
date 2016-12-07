# ！/usr/bin/env python3
# -*- coding:utf-8 -*-

# demo1
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICES = slice(31, 37)
cost = int(record[SHARES])*float(record[PRICES])
print(cost)
print(SHARES)
print('-'*15)

# demo2
items = [0,1,2,3,4,5,6,7]
a = slice(2,4)
print(items[2:4])
print(items[a])
items[a]=[10,11]
print(items)
del items[a]
print(items)
print('-'*15)

# demo3
s =slice(5,30,2)
print(s.start)
print(s.stop)
print(s.step)

str_ = 'HelloWorld'
print(s.indices(len(str_)))
for i in range(*s.indices(len(str_))):
    print(str_[i])