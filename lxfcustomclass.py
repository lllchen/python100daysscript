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
pass

'''