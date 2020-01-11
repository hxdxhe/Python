# -*- coding: utf-8 -*-
# @Time : 2020/1/11 16:44
# @Author : Aiopr
# @Email : 5860034@qq.com
# python2中导入
from collections import OrderedDict
from random import shuffle
from itertools import islice
d = OrderedDict()
d['c'] = 1
d['b'] = 2
d['a'] = 3
# print(list(iter(d)))
# print(d.keys())
players = list('abcdefg')
for i,p in enumerate(players,1):
    d[p] = i
print(d)

# print(shuffle(players))

class StudentInfo:
    def __init__(self):
        pass
    def __query_by_name(self,d,name):
        return d[name]


    def go(self,d,a,b=None):
        pass
        # print(self.__query_by_name(d,name))
        # print(self.__query_by_order(d,a,b))



b = islice(range(20),3,6)
# print(list(b))
def query_by_order(d, a, b=None):
    a -= 1
    if b is None:
        b = a + 1
    return list(islice(d, a, b))

b = query_by_order(d,3,6)
print(b)
