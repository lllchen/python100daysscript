#!/usr/bin/env python
#-*- coding = utf-8 -*-

'''

廖雪峰定制类练习


'''

__author__='BrilliantDawn'

'''
总结：
1.__slots__能固定类中的属性
2.__len__()方法能让类作用于len()函数
3.__str__()方法能让print不再打印对象的地址，而是定制化的内容，更好看
4.__repr__()方法与__str()__类似，区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
5.__iter__()方法能让类的实例作用于for...in...循环，也就是说可以把类变为iterable
6.__getitem__()方法能实现根据下标[i]取元素，也能实现切片操作。
7.__getattr__()方法能动态返回属性。
8.__call__方法可以实现对类实例的调用。

'''
import time


class BDcustomclass(object):
    __slots__ = ('__name','__sex','__birthday','__age','__address')

    def __init__(self,name,sex,birthday,address):
        self.__name = name
        self.__sex = sex 
        self.__birthday = birthday
        self.__age = time.localtime(time.time()).tm_year - int(birthday[0:4]) if time.localtime(time.time()).tm_mon > int(birthday[4:6]) else time.localtime(time.time()).tm_year - int(birthday[0:4])-1
        self.__address =address
    
    def __str__(self) -> str:
        return '名字：%s，性别：%s，生日：%s，年龄：%d，户籍：%s' % (self.__name,self.__sex,self.__birthday,self.__age,self.__address)



    pass


def main():
    lc = BDcustomclass('lc','man','19921231','tj')
    print(lc)


if __name__ == '__main__':
    main()
