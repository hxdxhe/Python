# -*- coding: utf-8 -*-
# @Time : 2020/3/2 11:47
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 1
from re import findall

from urllib.request import urlopen

url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx739bbc84f238563a&redirect_uri=http%3A%2F%2Fmxs.lanseeyun.com%2Fyx_auth.php%3FbaseUrl%3Dhttp%253A%252F%252Fshop.lanseeyun.cn%252F&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect'

with urlopen(url) as fp:

    content = fp.read().decode()

    pattern = 'data-type="png" data-src="(.+?)"'

result = findall(pattern, content)

for index, item in enumerate(result):

    with urlopen(str(item)) as fp:

        with open(str(index)+'.png', 'wb') as fp1:

            fp1.write(fp.read())
