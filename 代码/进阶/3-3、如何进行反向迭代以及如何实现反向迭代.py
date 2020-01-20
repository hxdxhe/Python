# -*- coding: utf-8 -*-
# @Time : 2020/1/20 15:30
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 3-3、如何进行反向迭代以及如何实现反向迭代
from decimal import Decimal
class FloatRange:
    def __init__(self,a,b,step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))
    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step
    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step
fr = FloatRange(2.0,3.0,0.2)
for x in fr:
    print(x)
print('-'*20)
for x in reversed(fr):
    print(x)
