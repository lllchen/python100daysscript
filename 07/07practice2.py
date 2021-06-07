#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

生成指定长度的验证码

0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
\u0030\u0031\u0032\u0033\u0034\u0035\u0036\u0037\u0038\u0039
\u0041\u0042\u0043\u0044\u0045\u0046\u0047\u0048\u0049\u004a
\u004b\u004c\u004d\u004e\u004f\u0050\u0051\u0052\u0053\u0054
\u0055\u0056\u0057\u0058\u0059\u005a
\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u006a
\u006b\u006c\u006d\u006e\u006f\u0070\u0071\u0072\u0073\u0074
\u0075\u0076\u0077\u0078\u0079\u007a

'''

__author__ = 'lllchen'


import random


def securityCode():
    while True:
        r = random.randrange(0,63)
        if  r < 10:
            randomN = '\\u00'+str(random.randrange(30,40))
            m = randomN.encode().decode('unicode_escape')
            print('数字')
            yield m
        elif r < 36:
            randomL = '\\u00'+str(hex(random.randrange(int('41',16),int('5b',16))))[-2:]#必须切片，要不带0x
            n = randomL.encode().decode('unicode_escape')
            print('大字母')
            yield n
        else:
            randomL = '\\u00'+str(hex(random.randrange(int('61',16),int('7b',16))))[-2:]#必须切片，要不带0x
            n = randomL.encode().decode('unicode_escape')
            print('小字母')
            yield n
        

if __name__ == '__main__':
    result = ''
    for i in range(0,4):
        result += next(securityCode())
    print(result)