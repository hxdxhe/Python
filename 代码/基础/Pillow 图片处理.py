# -*- coding: utf-8 -*-
# @Time : 2020/4/2 10:48
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : Pillow 图片处理
import requests
r = requests.get('http://www.douban.com/')
l = r.status_code
print(l)