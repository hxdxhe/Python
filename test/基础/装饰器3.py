#-*- coding:utf-8 -*-
import time
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper
@decorator #语法糖
def p1():
    print('This is decorator')
def p2(tes):
    print('This is decorator' + tes)
def p3(ts1,ts2):
    print('This is decorator' + ts1 + ts2)

p1()
p2(' hello')
p3(' aiopr',' storm')