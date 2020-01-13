#-*- coding:utf-8 -*-
# @Author : Aiopr
# @Email : 5860034@qq.com
from random import randint
a = {x: randint(60,100) for x in 'xyzabc'}
print(a)
# 第一种方法
# print(iter(a))
# print(a.keys())
b = zip(a.values(),a.keys())
# b = zip(a.itervalues(),a.iterkeys())#在内存使用上更优化些  在Python2中
# print(list(b))
c = sorted(list(b))
print(c)
print('\n')
# 第二种方法
print(a.items())
d = sorted(a.items(),key=lambda x:x[1])
print(d)