#-*- coding:utf-8 -*-
from tkinter import *
import random
import time
from numpy import *

# 反应时实验呈现刺激
test_text = ['C', 'V', 'B', 'N', 'C', 'V', 'B', 'N', 'C', 'V', 'B', 'N', 'C', 'V', 'B', 'N', 'C', 'V', 'B', 'N']
random.shuffle(test_text)
# 指导语
direct_text = """说明：
1、反应时（reaction time，简称 RT）是心理学中最常用的反
应变量之—，它是指刺激施于有机体之后到明显反应开始所需
要的时间。实验分为简单反应时和选择反应时。
2、简单反应时是指对呈现的单一的刺激，只作单一的反应，一
旦看到屏幕上出现字母‘A’，就迅速按下‘A’键；
选择反应时就是根据不同的刺激物，在多种反应方式中选择符合
要求的。看到出现的字母'CVBN'后，迅速按下相应的字母按键。
3、请先填写您的姓名和性别，填写完成后按下Caps Lock键！"""
# 反应按键、刺激呈现和反应时间、正确反应的时间列表
rea_list = []
sti_time = []
rea_time = []
correct_time = []


# 捕获键盘按键
def press_key(event):
    react_time = round(time.time(), 3)
    rea_time.append(react_time)
    print(event.char)
    rea_list.append(event.char)
    react_v.set(event.char)


# 刺激呈现
def stimulation(sti_text, show_time):
    l = Label(frame3, text=sti_text, width=50, height=20, bg='black', fg='white')
    l.pack()
    showtime = round(time.time(), 3)
    if sti_text in test_text:
        sti_time.append(showtime)
    root.update()
    root.after(show_time)
    l.pack_forget()


# 反应正确数量和时间的统计和输出
def react_statistics():
    if len(test_text) == len(rea_list):
        result_v.set('您完整的做完了实验！')
        count = 0
        for i in range(20):
            if test_text[i] == rea_list[i]:
                count += 1
                time_delta = rea_time[i] - sti_time[i]
                print(time_delta)
                correct_time.append(time_delta)
                react_ave = round(mean(correct_time), 3)
        count_v.set(count)
        time_v.set(react_ave)
    else:
        count_v.set('无')
        time_v.set('无')
        result_v.set('您没有全部做出反应！')


# 简单反应时
def simple_sti():
    stimulation('预备', 2000)
    for i in range(20):
        stimulation('A', 1000)
        random_time = random.randint(1000, 6000)
        stimulation('', random_time)
    l = Label(frame3, text='实验结束', width=50, height=20, bg='black', fg='white')
    l.pack()
    react_statistics()


# 选择反应时
def choice_sti():
    stimulation('预备', 2000)
    result_v.set('实验正在进行中！')
    for i in test_text:
        stimulation(i, 1000)
        random_time = random.randint(1000, 6000)
        stimulation('', random_time)
    l = Label(frame3, text='实验结束', width=50, height=20, bg='black', fg='white')
    l.pack()
    react_statistics()


# 界面创建
root = Tk()
# root.iconbitmap(r'C:\Users\Administrator\Desktop\ready\pika.ico')
root.title('心理学实验系列')
root.resizable(0, 0)
# 键盘事件
root.focus_set()
root.bind("<Key>", press_key)
# 变量值跟踪
var_list = ['count_v', 'time_v', 'react_v', 'result_v']
for i in var_list:
    locals()[i] = StringVar()
# 创建框架
for i in range(1, 6):
    locals()['frame' + str(i)] = Frame(root)
    locals()['frame' + str(i)].pack()
# 创建标签、按钮、输入框
title_l = Label(frame1, text='反应时实验', fg='red')
title_l.pack()
Label(frame1, text=direct_text, justify=LEFT).pack()
for i in ['姓名:', '性别:']:
    Label(frame1, text=i).pack(side='left')
    Entry(frame1).pack(side='left')
Button(frame2, text='简单反应时', width=24, command=simple_sti).pack(side='left')
Button(frame2, text='选择反应时', width=24, command=choice_sti).pack(side='left')
Label(frame3, textvariable=result_v, width=50, bg='red', fg='white').pack()
Label(frame3, textvariable=react_v, width=50, bg='red', fg='white').pack()
Label(frame4, text='正确反应数量：', width=12).pack(side='left')
Entry(frame4, width=34, textvariable=count_v).pack(side='left')
Label(frame5, text='平均反应时长：', width=12).pack(side='left')
Entry(frame5, width=34, textvariable=time_v).pack(side='left')
root.mainloop()