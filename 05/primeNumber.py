"""
输出2~99之间的素数
Version: 0.1
Author: brilliantDwan
Date: 2021-06-03
comment:埃氏筛选法
"""
l = list(range(2,100))
for i in l:
    l = list(filter(lambda x:x%i != 0 or x == i ,l))
print(l)
