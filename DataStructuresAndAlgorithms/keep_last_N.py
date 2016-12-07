# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import deque

# test deque
# using deque(maxlen=N) creates a fixed-size queue.When new items are added and the queue
# is full, the oldest item is automatically removed.
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
print('-'*15)

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

'''
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


if __name__ == '__main__':
    with open(r'../cookbook/somefile.txt') as f:
        for line, previous_lines in search(f, 'python', 5):
            for pline in previous_lines:
                print(pline, end='')
                print('-' * 20)
'''

