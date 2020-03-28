# -*- coding: utf-8 -*-
# @Time : 2020/3/19 8:14
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 继承和多态
class Animal():
    def run(self):
        print('Animal is running....')
class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

Animal = Animal()
Dog = Dog()
Cat = Cat()
Animal.run()
Dog.run()
Cat.run()


def run_twice(animal):
    animal.run()
    animal.run()
# run_twice(Animal)
# run_twice(Dog)
# run_twice(Cat)
def Tortise(Animal):
    pass
