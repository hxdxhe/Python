# -*- coding: utf-8 -*-
# @Time : 2019/12/27 8:58
# @Author : Aiopr
# @Email : 5860034@qq.com
# @Project : test
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 3
    BLUE = 4
# print(VIP.RED)
for v in VIP:
    print(v)