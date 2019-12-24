# from p.p1 import a
# print("hello Python")

# a =[1,2,3,4,5,6,7,8,9,10]
# # b = [a[0]:len(a):2]
# for i in range(0,len(a),2):
#     print(a[i])
# b = a[0:len(a):2]
# print(b)
# print(b)
# import sys
# def print(code):
#     print(code)
#
# print('python')
class Student():
    sum = 0
    name = ''
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # print("构造函数启动")
        # print(name)
        # print(age)
    # def student_info(self):
    #     print(self.name)
    #     print('\t')
    #     print(self.age)
    #     return
    def marking(self):
        self.__score = 90
        self.name = name
result = Student('storm',18)
# print(result.__dict__)
# print(Student.__dict__)



