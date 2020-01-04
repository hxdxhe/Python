# -*- coding: utf-8 -*-
# @Time : 2020/1/3 8:55
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : c4.py
# @Project : test
class C4:
    s = 66
    t = 99
    def __init__(self):
        pass
    def test(self):
        a = 1
        b = 2
        c = a + b + self.__class__.t
        return c
    @classmethod
    def plus_sum(self):
        e =   C4.t + C4.s
        return e


    print(test.__dict__)

st = C4()
print(C4.__dict__)
print('\n<<<')
print(st.test())
print(st.plus_sum())
print('\n>>>')
