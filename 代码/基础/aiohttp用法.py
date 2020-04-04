# -*- coding: utf-8 -*-
# @Time : 2020/4/4 9:34
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : aiohttp用法
import asyncio
from aiohttp import web
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s!' %request.match_info['name']
    return web.Response(body=text.encode('utf-8'))
async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('Get','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    ruuner = web.AppRunner(app)
    await ruuner.setup()
    srv = web.TCPSite(ruuner,'localhost',8000)
    await srv.start()
    print('Server started at http://127.0.0.1:8000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
