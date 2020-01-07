# -*- coding: utf-8 -*-
# @Time : 2019/12/17 9:21
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : p2.py
# @Project : test
# import p.p1
b = [[1,2,3],('b','c','d')]
for i in b:
    for x in i:
        if x == 'c':
            break
        print(x,end='|')