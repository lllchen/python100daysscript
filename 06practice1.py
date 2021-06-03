#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

计算最大公约数和最小公倍数的模块

'''

__author__ = 'lllchen'

def gcd(*numbers):
    least = min(numbers)
    for i in range(1,least+1):
        remainders = list(filter(lambda x: x%i == 0,numbers))
        if len(remainders) == len(numbers):
            gcd = i
    return gcd

if __name__ == '__main__':
    print(gcd(6,12,18))
