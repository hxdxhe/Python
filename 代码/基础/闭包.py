# -*- coding: utf-8 -*-
# @Time : 2019/12/28 10:00
# @Author : Aiopr
# @Email : 5860034@qq.com
def f1():
    a = 10
    def f2():
        return a
    return f2
s = f1()
# print(s)
# # print(s.__closure__)

# 求旅行者的步数
orign = 0
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = step + pos
        pos = new_pos
        return pos
    return go

tourist = factory(orign)
print(tourist(1))
print(tourist(3))
print(tourist(5))

