# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
li = re.split(r'[;,\s]\s*', line)
print(li)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# fields = re.split(r'(;,\s)\s*', line)  # ['asdf fjdk; afed, fjek,asdf, foo']
fields = re.split(r'(;|,|\s)\s*', line)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print(delimiters) # [' ', ';', ',', ',', ',', '']
line_new =''.join(v+d for v,d in zip(values,delimiters))
print(line_new) # asdf fjdk;afed,fjek,asdf,foo

li = re.split(r'(?:;|,|\s)\s*', line)
print(li) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
