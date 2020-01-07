#-*- coding:utf-8 -*-
import time
def decorator(func):
    def wrapper(*args,**kwargs):
        print(time.time())
        func(*args,**kwargs)
    return wrapper
@decorator #语法糖
def p1():
    print('This is decorator')

@decorator
def p2(tes):
    print('This is decorator' + tes)

@decorator
def p3(ts1,ts2):
    print('This is decorator' + ts1 + ts2)
@decorator
def p4(ts1,ts2,**kwargs):
    print('This is decorator' + ts1 + ts2)
    print(kwargs)

p1()
p2(' hello')
p3(' aiopr',' storm')
p4(' i am','p4',a = 1,b = 5, c = '1,2,3')