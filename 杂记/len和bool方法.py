#-*- coding:utf-8 -*-
class Test():
    def __bool__(self):
        return False
    def __len__(self):
        return True
    # print(len(Test()))
    print(bool(Test()))