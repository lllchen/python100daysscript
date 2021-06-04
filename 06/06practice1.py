#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

计算最大公约数和最小公倍数的模块

'''

__author__ = 'lllchen'

from functools import reduce

#最大公约数
def gcd(*numbers):
    least = min(numbers)
    for i in range(1,least+1):
        remainders = list(filter(lambda x: x%i == 0,numbers))
        if len(remainders) == len(numbers):
            gcd = i
    return gcd

#最小公倍数
def lcm(*numbers):
    largest = max(numbers)
    product = reduce(lambda x,y:x*y,numbers)
    for i in range(2,product//largest):
        lcm = i * largest
        remainders = list(filter(lambda x: lcm % x == 0,numbers))
        if len(remainders) == len(numbers):
            return lcm



if __name__ == '__main__':
    print(gcd(6,12,18,25))
    print(lcm(6,12,18,24))
