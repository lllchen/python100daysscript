#!/usr/bin/env python3
#-*-coding=utf-8-*-

'''
定义一个类描述平面上的点，并提供移动点和计算到另一点距离的方法

'''

__auther__ = 'BrilliantDawn'


import math

class spot():
    def __init__(self,x:int,y:int):
        self.__x = x
        self.__y = y

    def move(self):
        xory,n= input('请输入要移动的坐标维度和数值,逗号分隔:').split(',')
        if xory == 'x':
            self.__x += int(n)
        elif xory == 'y':
            self.__y += int(n)
        print('当前坐标为:(%s,%s)' % (self.__x,self.__y))
    
    def distance(self,anotherspot):
        d = math.sqrt((self.__x - anotherspot.__x)**2 +  (self.__y - anotherspot.__y)**2)
        return d

if __name__=='__main__':
    p1 = spot(1,2)
    p1.move()
    p2 = spot(-1,-2)
    #print('%:.2f' % (p1.distance(p2)))
    print('距离为',(p1.distance(p2)))