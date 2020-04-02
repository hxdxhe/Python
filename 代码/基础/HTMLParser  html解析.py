# -*- coding: utf-8 -*-
# @Time : 2020/4/2 10:05
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : HTMLParser  html解析

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from datetime import datetime
from pytz import utc
from pytz import timezone


class EventSearchParser(HTMLParser):
    Cons = []
    times = []
    locs = []
    Conference = {'h3': 0, 'time': 0, 'span': 0}  # FLAG：{'名称':0,'时间':0,'地点':0}

    def handle_starttag(self, tag, attrs):  # 首元素 <start>
        attrs = dict(attrs)
        if tag == 'h3' and 'class' in attrs:
            if attrs['class'] == 'event-title':  # 判断为事件，其字段数据为会议名字
                self.Conference['h3'] = 1
        if tag == 'time' and 'datetime' in attrs:  # 判断为日期
            cst_tz = timezone('Asia/Shanghai')
            utc_tz = timezone('UTC')
            dt = datetime.strptime(attrs['datetime'][:-6], '%Y-%m-%dT%H:%M:%S')  # str->datetime
            dt_utc = dt.replace(tzinfo=utc_tz)  # 添加时区0:00
            dt_Shanghai = dt_utc.astimezone(cst_tz)  # 转换为上海时区
            self.times.append(dt_Shanghai)
        if tag == 'span' and 'class' in attrs:
            if attrs['class'] == 'event-location':  # 判断为地点,其字段数据为地点
                self.Conference['span'] = 1

    def handle_data(self, data):  # 字段数据
        if self.Conference['h3'] == 1:
            self.Cons.append(data)
            self.Conference['h3'] = 0  # 更新FLAG:名称
        if self.Conference['span'] == 1:
            self.locs.append(data)
            self.Conference['span'] = 0  # 更新FLAG：地点


def url2html(url):
    with request.urlopen(url) as f:
        html = f.read().decode(encoding='utf_8')
    return html


def output(parser):
    i = 1
    for x, y, z in zip(parser.Cons, parser.times, parser.locs):
        print('%d ConferencesName:%s\nDate:%s\nLocation:%s\n' % (i, x, y, z))
        i += 1


parser = EventSearchParser()
url = 'https://www.python.org/events/python-events/'
htmlsource = url2html(url)
parser.feed(htmlsource)
output(parser)
