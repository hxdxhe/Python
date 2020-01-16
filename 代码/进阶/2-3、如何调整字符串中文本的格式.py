# -*- coding: utf-8 -*-
# @Time : 2020/1/13 16:23
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 2-3、如何调整字符串中文本的格式
import re

fn = open('./document/vmware.log','r', encoding='UTF-8')
txt = fn.read()
# print(txt)
l = re.sub('(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})','\g<m>/\g<d>/\g<y> ',txt)
print(l)