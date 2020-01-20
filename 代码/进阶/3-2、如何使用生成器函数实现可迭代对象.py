# -*- coding: utf-8 -*-
# @Time : 2020/1/18 17:01
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 3-2、如何使用生成器函数实现可迭代对象
from  collections.abc import  Iterable
class PrimeNumbers(Iterable):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        for k in range(self.a,self.b+1):
            if self.is_prime(k):
                yield k
    def is_prime(self,k):
        return False if k < 2 else all(map(lambda x:k%x,range(2,k)))
pn = PrimeNumbers(1,30)
for n in pn:
    print(n)
