# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))  # 3
print(c.keys())  # KeysView(ChainMap({'x': 1, 'z': 3}, {'z': 4, 'y': 2}))
print(list(c.keys()))  # ['x','z','y']
print(c.values())  # ValuesView(ChainMap({'z': 3, 'x': 1}, {'z': 4, 'y': 2}))
print(list(c.values()))  # [1,2,3]
print('-' * 15)

# Operations that mutate the mapping always affect the first mapping listed
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y'] # KeyError: "Key not found in the first mapping: 'y'"
print('-' * 15)

values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)  # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])  # 3

# Discard last mapping
values = values.parents
print(values['x'])  # 2

# Discard last mapping
values = values.parents
print(values['x'])  # 1
print(values)  # ChainMap({'x': 1})
print('-' * 15)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x']) #1
print(merged) #{'z': 3, 'x': 1, 'y': 2}
a['x'] = 13
print(merged['x']) #1, No change
