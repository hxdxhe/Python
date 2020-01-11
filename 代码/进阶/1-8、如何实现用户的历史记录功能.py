# -*- coding: utf-8 -*-
# @Time : 2020/1/11 17:13
# @Author : Aiopr
# @Email : 5860034@qq.com
#猜数字游戏  双端对联
from random import randint
from collections import deque
import pickle
def guess(n,k):
    if n == k:
        print('猜对了，这个数字是%d'%k)
        return True
    if n < k:
        print('猜大了，比%d小。'%k)
    elif n > k:
        print('猜小了，比%d大。'%k)
    return False
def main():
    n = randint(1,100)
    i = 1
    hq = deque([],5)
    fw = open('save.pkl','wb')
    while True:
        line = input('[%d]请输入一个数字:'%i)
        if line.isdigit():
            k = int(line)
            pickle.dump(hq.append(k),fw)
            i += 1
            if guess(n,k):
                break
        elif line == 'quit':
            break
        elif line == 'help':
            l = pickle.load(open('save.pkl','rb'))
            print(l)

if __name__ == '__main__':
    main()