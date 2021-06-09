#!/usr/bin/env python3
#-*- coding=utf-8 -*-

'''
定义一个类描述数字时钟

'''

__auther__ = 'BrilliantDawn'

import time

class numClock(object):
    def __init__(self) -> None:
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0

    def run(self):
        while True:
            self.__hours = time.localtime(time.time()).tm_hour
            self.__minutes = time.localtime(time.time()).tm_min
            self.__seconds = time.localtime(time.time()).tm_sec
            print(f'{self.__hours}:{self.__minutes}:{self.__seconds}')
            time.sleep(1)


if __name__ == '__main__':
    lc = numClock()
    lc.run()