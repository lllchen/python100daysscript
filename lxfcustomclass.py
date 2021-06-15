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
5.__iter__()方法能让类的实例作用于for...in...循环，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。下面的定制类展示了两种__iter__实现方法，第一种是直接把它定义为一个生成器，这样就不用再使用StopIteration终止循环。
另一种是配合__next__()方法，不断返回下一个。
6.__getitem__()方法能实现根据下标[i]取元素，也能实现切片操作。
7.__getattr__()方法能动态返回属性。
8.__call__方法可以实现对类实例的调用。

'''
import time


class BDcustomclass(object):
    __slots__ = ('__name','__sex','__birthday','__age','__address','__fib_a','__fib_b')

    def __init__(self,name,sex,birthday,address,fib_a=0,fib_b=1):
        self.__name = name
        self.__sex = sex 
        self.__birthday = birthday
        self.__age = time.localtime(time.time()).tm_year - int(birthday[0:4]) if time.localtime(time.time()).tm_mon > int(birthday[4:6]) else time.localtime(time.time()).tm_year - int(birthday[0:4])-1
        self.__address =address
        self.__fib_a = fib_a
        self.__fib_b = fib_b
    
    def __len__(self):
        return len(self.__name+self.__sex+self.__birthday+self.__age+self.__address)
  
    def __str__(self) -> str:
        return '名字：%s，性别：%s，生日：%s，年龄：%d，户籍：%s' % (self.__name,self.__sex,self.__birthday,self.__age,self.__address)
    
    __repr__ = __str__

    #def __iter__(self):
    #    yield self.__name
    #    yield self.__sex
    #    yield self.__birthday
    #    yield self.__age
    #    yield self.__address

    def __iter__(self):
        return self
    
    def __next__(self):
        self.__fib_a ,self.__fib_b = self.__fib_b,self.__fib_a+self.__fib_b
        if self.__fib_a>99999:
            raise StopIteration()
        return self.__fib_a

    pass


def main():
    lc = BDcustomclass('lc','man','19921231','天津')
    print(lc)
    for i in lc:
        print(i)

if __name__ == '__main__':
    main()
