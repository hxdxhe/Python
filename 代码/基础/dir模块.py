# -*- coding: utf-8 -*-
# @Time : 2020/3/26 10:43
# @Author : Aiopr
# @Email : 5860034@qq.com
# @File : dir模块
#利用os模块编写一个能实现dir -1输出的程序。

import os
import time

def TimeStampToTime(timestamp):
    timeStruct=time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)


def Get_FileModifyTime(filepath):
    t=os.path.getmtime(filepath) #出错：找不到文件夹的修改时间
    #t=os.stat(filepath).st_mtime #功能同上
    return TimeStampToTime(t)


def Get_FileSize(filepath):
    if os.path.isdir(filepath):
        size='<DIR>'
    elif os.path.isfile(filepath):
        size=os.path.getsize(filepath)
    return size

def Get_FileName(filepath):
    name=os.path.split(filepath)[1]
    return name

def main():
    listPath='.'
    list_A=os.listdir(listPath)
    # list_A=map(lambda x:os.path.join(listPath,x),list_A) #若无这一行，会出现错误：[WinError 2] 系统找不到指定的文件
    list_A=[os.path.join(listPath,x) for x in list_A]
    total_size=0
    for file in list_A:
        print('%10s %10s %-10s' % (Get_FileModifyTime(file), Get_FileSize(file), Get_FileName(file)))
        if isinstance(Get_FileSize(file),int):
            total_size=total_size+Get_FileSize(file)

    file_num=len([x for x in list_A if os.path.isfile(x)])
    dir_num=len([x for x in list_A if os.path.isdir(x)])
    print('%d个文件,共%d字节' % (file_num,total_size))
    print('%d个目录' % dir_num)

if __name__=='__main__':
    main()