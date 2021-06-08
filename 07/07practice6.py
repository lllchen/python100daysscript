#!usr/bin/env python3
#-*- coding = utf-8 -*-


'''
打印杨辉三角
'''


__auther__ = 'BrilliantDawn'

def yangTriangle():
    yield [1]
    l = [1,1]
    while True:
        yield l
        temp =[1]
        for i in range(len(l)-1):
            temp.append(l[i]+l[i+1])
        temp.append(1)
        l = temp


if __name__ == '__main__':
    yt = yangTriangle()
    for i in range(10):
        print(next(yt))
