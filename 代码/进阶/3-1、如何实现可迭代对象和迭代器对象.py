# -*- coding: utf-8 -*-
# @Time : 2020/1/18 15:03
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 3-1、如何实现可迭代对象和迭代器对象
from collections.abc import Iterable,Iterator
import requests
class WeatherIteraor(Iterator):
    def __init__(self,caties):
        self.caties = caties
        self.index = 0
    def __next__(self):
        if self.index == len(self.caties):
            raise StopIteration
        city = self.caties[self.index]
        self.index += 1
        return self.get_weather(city)
    def get_weather(self,city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city,data['high'],data['low']
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIteraor(self.cities)
def show(w):
    for x in w:
        print(x)

w = WeatherIterable(['包头','呼和浩特','鄂尔多斯']*10)
show(w)

