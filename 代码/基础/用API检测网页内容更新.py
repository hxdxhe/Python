# -*- coding: utf-8 -*-
# @Time : 2019/12/31 15:05
# @Author : Aiopr
# @Email : 5860034@qq.com
import requests
import webbrowser
import time

api = 'https://api.github.com/repos/soimort/you-get'  # API地址
web_page = 'https://githubK.com/soimort/you-get'  # 项目地址

# last_update = None
last_update = '2019-12-24T20:51:16Z'  # 为了测试效果直接赋值一个时间。
all_info = requests.get(api).json()  # 转换获取到的API数据为pyhon能识别的字典型数据结构

# dict_info=all_info.json()   //相当于上面的模式"requests.get(api).json()"赋值转换

# cur_update = all_info['updated_at']
"""这里蕴含一个字符串也可以比大小的知识，需要相同格式的字符串比大小，是能正常比对的！
这里还用到了字典列表，all_info['updated_at']就是取了all_info里面的字典对应的键值（还没理解……）

"""
# print(cur_update)
# while True:  # 无限循环检测
#
#     if not last_update:  # 这里判断last_update的值是否存在
#         last_update = cur_update  # 判断两边的（不理解……）
#
#     if last_update < cur_update:  # 判断两边的值的大小
#         webbrowser.open(web_page)  # 如果last_update的值小于cur_upate的值则打开项目地址页面
#
#         time.sleep(600)  # 程序睡眠600s 也算是暂停600s再继续循环执行