#！/usr/bin/env python3
#-*- coding:utf-8 -*-
from collections import defaultdict

dl = defaultdict(list)
dl['a'].append(1)
dl['a'].append(2)
dl['b'].append(4)
print(dl)
ds = defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)
ds['b'].add(4)
print(ds)

'''
d = {}
for key,value in pairs:
    if key not in d:
    d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
'''