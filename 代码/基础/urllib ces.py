# -*- coding: utf-8 -*-
# @Time : 2020/4/1 16:02
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : urllib
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))