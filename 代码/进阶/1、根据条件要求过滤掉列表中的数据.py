# -*- coding: utf-8 -*-
# @Time : 2020/1/7 10:39
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : c1.py
# @Project : Python_pro
# 找出列表中的大于0的数
from random import randint
l = [randint(-10,10) for _ in range(10)]  # 在循环体重没有用到变量 用下划线_代替
# print(l)
# 第一种方法 列表解析
k = [x for x in l if x >= 0]
# print(k)
# 第二种方法  内置filter函数
z = filter(lambda x: x >= 0, l)
# print(list(z))
# 第三种方法字典
# 知道一个班的分数，求出大于90
a = {'studend%d' % i: randint(50,100) for i in range(1,21)}
b = {k:v for k,v in a.items() if v >= 90}
# 用filter表示
c = filter(lambda item:item[1] >= 90,a.items())  #由于lambda中只能传一个值，所以只能是选取一个值【1】
# print(dict(c))
# 第四种方法集合
#找出能整除3的数
s = {randint(0,20) for _ in range(20)}
d = {x for x in s if x % 3 == 0}
print(d)
