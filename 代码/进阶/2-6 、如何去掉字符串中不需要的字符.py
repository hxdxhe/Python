# -*- coding: utf-8 -*-
# @Time : 2020/1/17 11:00
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 2-6 、如何去掉字符串中不需要的字符
import re
import unicodedata
# 方法一 用函数strip
txt = '   wfwox3202'
l = txt.strip()
print(l)
# 方法二 用切片
t = 'Miracles sometimes occur, but one ++ has to work terribly for them.'
st = t[:33]+t[36:]
print(st)
# 方法三 用正则表达式
l = re.sub('[+]+','',t)
print(l)
#方法三 用translate方法
a = 'abc123xyz' #把小写转换成大写
l = a.maketrans('abcxyz','ABCXYZ') #把小写转换成大写
b = a.translate(l)
print(b)
c = a.translate({ord('a'):None}) #删除需要删除字符串
print(c)

d = 'shū rù nín yào zhuǎn huàn de hàn zì nèi róng'
n= "ū"
# print(n[1])
m = unicodedata.normalize('NFKD', d).encode('ascii','ignore')
print(m)
