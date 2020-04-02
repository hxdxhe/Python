# -*- coding: utf-8 -*-
# @Time : 2020/3/28 16:09
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 正则
import re
def is_valid_email(addr):
    res = re.match(r'([\w\.]+@([\w\.\w]+))',addr)
    res1 = re.match(r'<?([\s\w]+)>?[\s\w]*@(\w+\.?\w+)',addr)
    res2 = re.match(r'<?([\s\w]+)>?[\s\w]*@(.*)', addr).group(1)
    if(res):
        return True
    else:
        return False
is_valid_email('someone@gmail.com')



