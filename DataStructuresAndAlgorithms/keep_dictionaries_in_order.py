# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import OrderedDict


def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['gork'] = 4
    for key in d:
        print(key, d[key])
    return d

od = ordered_dict()

import json
print(json.dumps(od))

# Be aware that the size of an OrderedDict is more than twice as large as a normal dictionary
# due to the extra linked list that's created.