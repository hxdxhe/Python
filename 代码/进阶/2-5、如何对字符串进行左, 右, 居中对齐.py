# -*- coding: utf-8 -*-
# @Time : 2020/1/16 15:50
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 2-5、如何对字符串进行左, 右, 居中对齐
# 方法一
txt = 'abc'
l = txt.rjust(10,'*')
print(l)
# 方法二
m = format(txt,'*<10') #左对齐，
m = format(txt,'*^10') #居中对齐

n= format(-123,'^=+10') # 加个等号可以使负号向左填充字符在等号右边
print(n)
print(m)

#实际使用
d = {'sfwft':100,'lfwr':46,'twfewm':99,'smfwegxwfew':64}
w = max(map(len,d.keys())) #迭代所有的键，获取键的最宽的那个数值，用最宽的那个数值进行对齐
for k,v in d.items():
    print(k.ljust(w),':',v)