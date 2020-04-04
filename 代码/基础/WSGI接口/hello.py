# -*- coding: utf-8 -*-
# @Time : 2020/4/3 16:50
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : hello
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]