# -*- coding: utf-8 -*-
# @Time : 2020/4/1 14:11
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 计算圆周率
import itertools
from functools import reduce
def pi(N):
    #' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1,2) #创建一个从1开始每次的步长是2的无穷序列
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # lodd = itertools.takewhile(lambda x : x < = 2*N -1,odd)
    lodd = itertools.takewhile(lambda x: x <= 2 * N - 1, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    nums = itertools.cycle((4,-4))
    s3 = [nums.__next__()/i for i in lodd]


    # step 4: 求和:
    sum = reduce(lambda x,y:x+y,s3)
    return sum

assert 3.04 < pi(10) < 3.05