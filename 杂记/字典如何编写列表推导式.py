#-*- coding:utf-8 -*-
students={
    '喜小乐':18,
    '石敢当':20,
    '横小五':15
}

b = {value:key for key,value in students.items()} #字典的话循环要有两个值,而且注意item()方法  要显示字典这里用{}括号
print(b)