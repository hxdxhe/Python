# -*- coding: utf-8 -*-
# @Time : 2019/12/17 9:21
# @Author : Aiopr
# @Email : 5860034@qq.com
# import p.p1
b = [[1,2,3],('b','c','d')]
for i in b:
    for x in i:
        if x == 'c':
            break
        print(x,end='|')