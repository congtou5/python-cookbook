# ！/usr/bin/env python3
# -*- coding:utf-8 -*-

# demo1
def drop_first_last(grades):
    first, *middle, last = grades
    return middle


dec_grades = [90, 85, 94, 88, 99]
print(drop_first_last(dec_grades))
print('---------')

# demo2
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

print('----------')

# demo3
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print('-----------')

# demo4
record = ['ACME', 50, 91.1, (21, 12, 2012)]
name, *_, (*_, year) = record
print(name)
print(year)
print('-------------')

# demo5
items = [1, 10, 7, 4, 5, 9]


def sum_(items):
    head, *tail = items
    return head + sum_(tail) if tail else head


print(sum_(items))
