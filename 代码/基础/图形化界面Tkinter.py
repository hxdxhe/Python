# -*- coding: utf-8 -*-
# @Time : 2020/4/3 9:00
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 图形化界面Tkinter
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self):
        Frame.__init__(self,master=None)
        self.pack()
        self.creatWidgets()
    def creatWidgets(self):
        self.helloLabel = Label(self,text='Hello,world')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='退出',command=self.hello)
        self.quitButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)
app = Application()
app.master. title('测试程序')
app.mainloop()
