# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)  # A counter is a dictionary
top_three = word_counts.most_common(3)
print(top_three)  # Outputs [('eyes', 8), ('the', 5), ('look', 4)]
print(word_counts['my'])
print(word_counts['eyes'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
print(word_counts['eyes'])
print('-' * 15)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
c = a + b
print(c)
d = a - b
print(d)
