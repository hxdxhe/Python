# -*- coding: utf-8 -*-
# @Time : 2020/1/18 15:03
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 3-1、如何实现可迭代对象和迭代器对象
import requests
url = 'http://wthrcdn.etouch.cn/weather_mini?city=包头市'
r = requests.get(url)
print(r.json())