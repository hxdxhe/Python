# -*- coding: utf-8 -*-
# @Time : 2019/12/22 10:24
# @Author : Aiopr
# @Email : 5860034@qq.com
class Student():
    sum = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.sum += 1
        print(self.name +'的年龄为'+str(self.age)+ '成绩为'+str(self.__class__.sum))
    def do_homework(self):
        print('english homework')
    def marking(self):
        self.__score = 0

result = Student('小明',18)
