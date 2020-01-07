#-*- coding:utf-8 -*-
import time
def f1():
    print("This is function")
def f2():
    print("This is function too")
def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)