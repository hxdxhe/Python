# -*- coding: utf-8 -*-
# @Time : 2020/3/26 17:40
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
