# -*- coding: utf-8 -*-
# @Time : 2020/4/3 10:02
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 画星星
from turtle import *

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()