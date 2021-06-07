#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
根据年月日算天数

'''

__auther__='BrilliantDawn'

def countDays(year,month,days):
    if year%400==0 or (year%100!=0 and year%4 == 0):
        dic = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    else:
        dic = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    sum = 0
    for i in range(1,month):
        sum += dic[i]
    sum += days
    return sum


if __name__=='__main__':
    print(countDays(2021,6,7))