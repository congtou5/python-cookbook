#！/usr/bin/env python3
#-*- coding:utf-8 -*-

# ***demo1***
filename = 'spam.txt'
print(filename.startswith('spam'))
print(filename.endswith('.txt'))

# ***demo2***
import os
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.py','.c'))])
print(any(fn.endswith('.py') for fn in filenames ))

# ***demo3***
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read
    else:
        with open(name) as f:
            return f.read()

# startswith first arg must be str or a tuple of str, not list;
# endswith like startswith