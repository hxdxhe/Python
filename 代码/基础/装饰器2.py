#-*- coding:utf-8 -*-
import time
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

def p1():
    print('This is decorator')

d1 = decorator(p1)
d1()