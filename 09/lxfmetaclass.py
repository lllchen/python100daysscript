#!/usr/bin/env python3
#-*- coding = utf-8 -*-

'''
廖雪峰元类练习

下面的-->代表“实例”关系，不是继承关系。
type-->int -->1
type-->Metaclass-->Commonclass
type-->EnumMeta-->Enum or Customclass -->  Customclass.__members__
写代码的时候Customclass继承自Enum，type函数的结果显示Enum和Customclass都由EnumMeta“实例”而来，
'''

__auther__ = 'BrilliantDawn'


def fn(self,name = 'world'):
    print('Hello,%s' % name)

Hello = type('Hello1',(object,),dict(hello=fn))
Hello2 = type('Hello2',(Hello,),dict())

if __name__ == '__main__':
    h = Hello()
    h.hello()
    h2 = Hello2()
    h2.hello()
    pass