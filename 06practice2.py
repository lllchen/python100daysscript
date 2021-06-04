#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

判断回文数

'''

__author__ = 'lllchen'

def getsingle(number):#得到每位数
    while number > 0:
        yield number%10
        number //= 10

def pn(number):
    r = 0
    for i in getsingle(number):
        r =r*10 + i
    return r == number

if __name__ == '__main__':
    print(pn(120321))
    