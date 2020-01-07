# -*- coding: utf-8 -*-
# @Time : 2019/12/24 16:39
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : zongjie.py
# @Project : test
__all__=('A','B','cs')
class A():
    def __init__(self):
        print('类A')
    def test(self):
        print('测试方法')
class B():
    def __init__(self):
        print("类B")
    def student(self,name,age):
        self.name = name
        self.age = age
def cs():
    print('类外的方法')