#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''

判断素数

'''

__author__ = 'brilliantDawn'

def judgePrimeNumber(n):
    l=range(2,n)
    for i in l:
        l = filter(lambda x : x%i != 0 or x == i,l)
    for i in l:
        if n % i == 0:
            return False
    return True if n!=1 else False

if __name__ == '__main__':
    print(judgePrimeNumber(1))