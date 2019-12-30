#-*- coding:utf-8 -*-
# none无论从类型上还是值上都不等于空字符串或空列表、False、  0

a = []
if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')