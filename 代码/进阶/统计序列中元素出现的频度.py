# -*- coding: utf-8 -*-
# @Time : 2020/1/9 11:25
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : 统计序列中元素出现的频度.py
# @Project : Python_pro


# 方法一
from random import  randint
from collections import Counter
import re
data = [randint(0,20) for _ in range(30)]
# print(data)
# print('\n')
# c = dict.fromkeys(data,0)  #以data作为键，0作为初始值创建一个列表
# print(c)
# for x in data:
#     c[x] += 1 #出现一次+1
# print('\n')
# print(c)

# 方法二
# 统计出现的次数
c = Counter(data)
# 统计出现频率最高的三个
d = c.most_common(3)


# 案例二：英文文章词频统计
txt = open('story.txt').read()
txt = Counter(re.split('\W+',txt))
print(txt.most_common(3))
