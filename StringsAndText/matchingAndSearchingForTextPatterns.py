# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

# You can use str.find(),str.startswith(),str.endswith()
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
print('-' * 15)

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013'
print(datepat.match(text3))  # Outputs:None
print(datepat.findall(text3))
print('-' * 15)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.groups())
print(m.group(3))
print('-' * 15)

print(datepat.findall(text3))
for month, day, year in datepat.findall(text3):
    print('{}-{}-{}'.format(year, month, day))
for m in datepat.finditer(text3):
    print(m.groups())