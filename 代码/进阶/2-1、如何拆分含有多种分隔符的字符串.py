# -*- coding: utf-8 -*-
# @Time : 2020/1/13 11:12
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 2-1、如何拆分含有多种分隔符的字符串
from functools import  reduce
import re

s  =  'wefw,.fewi/efw\tleww.s;lug;fwg'
# print(s.split(';'))
t = []
l = [x.split(';') for x in s.split(',') ]
# map(lambda x,y:x.split(y),s.split())
def my_splits(s,seps):
    res = [s]  # 把字符串放入列表中
    for sep in seps:
       t = []
       list(map(lambda ss:t.extend(ss.split(sep)),res)) #用map迭代这个列表，因为split生成的是个二维列表，所以需要extend函数组成一维继续使用  map函数出来的是个对象 需要用list函数来显示
       res = t
    return res
b = my_splits(s,',./\t;')
print(b)
d = re.split('[,./\t;]+',s)  #用正则表达式
print(d)