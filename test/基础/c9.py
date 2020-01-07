# -*- coding: utf-8 -*-
# @Time : 2019/12/23 14:43
# @Author : LiDong
# @Email : 5860034@qq.com
# @File : c9.py
# @Project : test
# 从字符串中找到数字，大于6返回9 小于6返回0
import re
a ='AD8765WEFF47WF782479WFE96G3XG61GW'

def findnum(self):
    match = self.group()
    # print(match)
    if int(match) >= 6:
        return '9'
    else:
        return '0'
r = re.sub('\d',findnum,a)
print(r)
# findnum(a)