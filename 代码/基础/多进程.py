# -*- coding: utf-8 -*-
# @Time : 2020/3/26 17:05
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : 多进程
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc,args=('System',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')