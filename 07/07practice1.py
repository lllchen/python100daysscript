#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

屏幕显示跑马灯

'''

__auther__ = 'brilliantDawn'


import os
import time

def main():
    content = '不要放弃啊！！！！！'
    while True:
        os.system('cls')#清除屏幕内容
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]
    
if __name__ == '__main__':
    main()