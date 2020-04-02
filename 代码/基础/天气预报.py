# -*- coding: utf-8 -*-
# @Time : 2020/4/2 9:44
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 天气预报


#请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
#http://www.weather.com.cn/textFC/hb.shtml#
#参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。
from xml.parsers.expat import ParserCreate
from urllib import request