# -*- coding: utf-8 -*-
# @Time : 2020/1/11 14:40
# @Author : Aiopr
# @Email : 5860034@qq.com
from random import randint,sample
from functools import reduce
# print(sample('abcdefgh',3))   #随机获取字符串中的3个元素
l = sample('abcdefg',randint(3,6))
# print(l)
b1 = {k:randint(1,4) for k in l}
b2 = {k:randint(1,4) for k in l}
b3 = {k:randint(1,4) for k in l}
b4 = [b1,b2,b3]
# print(b4)
#列表解析表达式 [表达式  for 元素 in 可迭代对象  if 条件]
m = [k for k in b1 if k in b2 and k in b3]
print(m) #此方法只能指定目标
# 方法一
a = [k for k in b4[0] if all(map(lambda d: k in d,b4[1:]))]
print(a)
# 方法二  用集合交集 reduce函数
# c = reduce(lambda a,b:a*b,range(1,11))  #用reduce求1到11的阶乘
# print(c)
d =reduce(lambda a,b:a & b,map(dict.keys,b4))
print(d)