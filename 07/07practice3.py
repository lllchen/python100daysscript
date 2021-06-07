#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
返回指定文件名的后缀

'''

__auther__='brilliantDawn'

def getSuffix(name:str):
    index = name.find('.')
    return name[index+1:]

if __name__ == '__main__':
    print(getSuffix('python.py'))