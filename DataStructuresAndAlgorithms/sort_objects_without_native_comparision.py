#！/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
对不支持原生比较的对象排序
'''

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(10), User(6), User(55)]
    print(users)
    print(sorted(users, key = lambda u: u.user_id))

sort_notcompare()
print('-'*15)

# Quicker way
from operator import attrgetter
users = [User(10), User(6), User(55)]
print(sorted(users, key=attrgetter('user_id')))

# Also be applied to functions such as min() and max()
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))