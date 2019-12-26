# -*- coding: utf-8 -*-
# @Time : 2019/12/24 8:14
# @Author : Storm
# @Email : 5860034@qq.com
# @File : 总结.py
# @Project : test
from zongjie import B
class Review(B):
    def __init__(self):
        super(Review, self).__init__()
    # 进制转换
    def jinzhi(self):
        num = 99
        # 二进制
        print(bin(num))
        # 八进制
        print(oct(num))
        # 十进制
        print(int(num))
        # 十六进制
        print(hex(num))
    def string(self):
        a = '字符串换\
行'
        print(a)
        # 转义字符
        b = '我是\n一个\'很长\t的字\r符串'
        print(b)
        print(r'前面加上r\n就没用了')
        # 字符串运算
        c = 'hello world'
        print(c[0:5])
        print(c[0:-1])
        print(c[6:])
        # 列表
        d = ["00","11",'22','33']
        print(d[0])
        print(d[0:2])
        #元组
        e = ('hello',"python","love",'life','C')
        print(e[0])
        print(e[0:2])
        print(e[0:5:2])
        e1 = 'love'
        e2 = 'php'
        print(e1 in e) #是否在字符串内
        print((e2 not in e))#是否不在字符串内
        print(len(e))#字符串长度
        print(max(e))  #最大字符串
        print(min(e)) #最小字符串
        print(ord('a')) #ASCII码地址
        # 集合
        f = {'python','php','javascript','java','C#'}  #数据不能重复
        #判断用in  not in
        print('python' in f)
        print('php' not in f)
        # 字典
        g = {0:'看书',1:'打篮球',2:'爬山',3:'跑步'}
        print(g[1])  #访问序号就能访问value值
    # 变量
    def bianliang(self):
        # 两个区别：
        #     ①int、str、tuple是值类型，是不可变的，list、set、dict是引用类型 是可变的
        #     ②列表可以用append()追加元素，元组不可追加元素，元组不可变，列表可变
        h = 'wefewij908wfew'
        h1 = ['2s','2se']
        isinstance(h,int) #判断变量的类型 返回bool类型
        isinstance(h1,int) #判断变量的类型
        print(type(h))
    #条件判断
    def flow(self):
        j = "854wef969fwe687w66wefgw7s"
        j1 = ['文峰违','storm','ariopr']
        j2 = {1:'s',2:'e',3:'p'}
        for i in j1:
            # print(i)
            if i == 'storm':
                continue
            print(i,end='|')
        print('\n')
        j3 = 0
        while j3 <= 10:
            j3 += 1
            print(j3,end="|")
        print('\n')
        for j in j2:
            print(j2[j],end="/")
        # 数字循环
        print('\n')
        for k in range(0,10,3):
            print(k,end='/')
    def parent(self,name,age):
        print('This is parent class')
        super(Review,self).student(name,age)


result = Review()
# result.jinzhi()
# result.string()
# result.flow()
result.parent('storm',18)