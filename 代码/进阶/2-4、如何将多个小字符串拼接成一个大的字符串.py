# -*- coding: utf-8 -*-
# @Time : 2020/1/16 15:18
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 如何将多个小字符串拼接成一个大的字符串
from functools import reduce
txt = ['<034>','<038>','<785>','<894>','<opxe>']
# 方法一
str = ''
for x in txt:
    str += x
# print(str)

# 方法二
l = ''.join(txt) #''内是连接符，
print(l)
