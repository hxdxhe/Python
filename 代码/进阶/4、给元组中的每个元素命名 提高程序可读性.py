# -*- coding: utf-8 -*-
# @Time : 2020/1/10 8:56
# @Author : Aiopr
# @Email : 5860034@qq.com
from enum import IntEnum
from collections import namedtuple
# 第一种 枚举
s = ('jim',16,'male','jim896@gmail.com')
class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3
# a = StudentEnum()
print(s[StudentEnum.NAME])
print('\n')
# 第二种 用标准库中的namedtuple元组
Student = namedtuple('Student',['name','age','sex','email'])
s2 = Student('jim',16,'male','jim896@gmail.com')
print(isinstance(s2,tuple))  #isinstance函数来判断一个对象是否是一个已知的类型  
print(s2.name)