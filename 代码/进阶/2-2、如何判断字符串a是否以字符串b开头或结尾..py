# -*- coding: utf-8 -*-
# @Time : 2020/1/13 14:14
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 2-2、如何判断字符串a是否以字符串b开头或结尾.
import os
import stat
a = os.listdir('./document/')  #括号中写入路径，如果是当前直接留空就行
# print(a)
s = os.stat('./document/index.html')
print(s) #读取系统属性信息
for fn in a:
    if fn.endswith(('.html','.pkl','.js','.txt')):
        fs = os.stat(fn) #读取文件状态  文件属性
        os.chmod(fn,fs.st_mode | stat.S_IXUSR) #修改文件权限


