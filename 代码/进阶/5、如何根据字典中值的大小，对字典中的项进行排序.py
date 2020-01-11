# -*- coding: utf-8 -*-
# @Time : 2020/1/11 9:06
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : 5、如何根据字典中值的大小，对字典中的项进行排序.py
# @Project : Python_pro
from random import randint
# 方案一：将字典中的项转换成（键、值）元组。列表解析或者zip
n = {x:randint(60,100) for x in 'abcdefghi'}
print(n)
m = zip(n.values(),n.keys())
m = sorted(list(m),reverse=True)
print(m)
print('\n')

# 方法二 传递sorted函数的key参数
p = sorted(n.items(),key=lambda item:item[1],reverse=True)
d = list(enumerate(p,1))
# print(c)

# for i , (k , v) in enumerate(p,1):
#     n[k] = (i,v)    #？？？？？问题  n不排序
#     # print(i,k,v)
# print(n)
d = {k:(i,v) for i,(k,v) in enumerate(p,1)}
print(d)