# -*- coding: utf-8 -*-
# @Time : 2019/12/22 14:37
# @Author : Aiopr
# @Email : 5860034@qq.com
import re
a = 'C|C++|Java|C#|Python|PHP'
b = 'wefhweoifhwf9u7989&*7__--++==wejffew'
r= re.findall('Python',a)
s = re.findall('\w',b)
# if len(r) > 0:
#     print('字符串中包含Python')
#     print(r)
print(len(s))
print(s)
