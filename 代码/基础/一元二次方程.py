# -*- coding: utf-8 -*-
# @Time : 2020/3/7 16:39
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 一元二次方程

import math
while True:
    a = int(input("请输入第一个参数a："))
    b = int(input("请输入第二个参数b："))
    c = int(input("请输入第三个参数c："))
    def quadratic(a, b, c):
        d = b**2-4*a*c
        if a == 0:
            print("方程a系数不能等于0")
            return

        #该方程在实数域内有两个不相等的实数根：
        if d > 0:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            print("此方程有两个不相等的实数根为：",x1,x2)
        #该方程在实数域内有两个相等的实数根
        elif d == 0:
           x = (-b)/(2*a)
           print("此方程有一个实数根为：",x)
        #该方程在实数域内无解
        else:
           print("此方程无解")

    quadratic(a,b,c)