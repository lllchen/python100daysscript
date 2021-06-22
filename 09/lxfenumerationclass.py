#!/usr/bin/env python3
# -*- coding=utf-8 -*-

'''
廖雪峰枚举类练习

Month是一个枚举对象
这个对象的成员是Month999.Jan一系列。
每个成员的名称叫Jan一系列。
成员的值是1,2,3,4,5...默认都从1开始，因为有auto()方法默认从1开始指定值。
特殊属性 __members__ 是一个从名称到成员的只读有序映射。 它包含枚举中定义的所有名称，包括别名（如果有两个成员的值相同，名字不同，那后面成员的名字就是前面成员的别名）。
@unique装饰器，会搜索一个枚举的 __members__ 并收集所找到的任何别名；只要找到任何别名就会引发 ValueError 并附带相关细节信息。

详见：https://docs.python.org/zh-cn/3/library/enum.html#enum.unique

'''

__auther__ = 'BrilliantDawn'

from enum import Enum,EnumMeta,unique
from types import MappingProxyType#不可变的映射类型，可将普通的dict集合变为元素值不能变得集合，详见d_view。Enum的成员集合就是这个类型。

Month = Enum('Month999',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))#ed2
#上面这句好像就是创建了一个叫Month999的‘类’，而且好像enum并不是常规的类，详见for里两个type的运行结果。
#但是Month999这个‘类’好像又不是‘显示’的（自创名字，姑且这么叫），因为ed1行执行会报错，使用Enum的构建函数创造一个对象的方式来建立一个Enum好像和定制一个Enum类区别不大，
#但是还是有区别，如果真是用创建类的方式继承自Enum的Month999，那这个名字就能‘显示’的使用，不想在这，还得用Month.__members__调用。

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value,';type:',type(member),type(1))


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d_view = MappingProxyType(d)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

test = Weekday#这么一整，test好像就和ed2里的Month一样了

print('Month.__members__:',Month.__members__)
print('type(Month.__members__):',type(Month.__members__))
print('Month.__members__[\'Jan\']:',Month.__members__['Jan'])
print('type(Month.__members__[\'Jan\']',type(Month.__members__['Jan']))
print('type(Month.__members__[\'Jan\'].value',type(Month.__members__['Jan'].value))
print('type(Month):',type(Month))
#print(Month999.Jan)#ed1

print('d:',d)
print('type(d):',type(d))
print('d_view:',d_view)
print('type(d_view):',type(d_view))

print('Weekday:',Weekday)
print('type(Weekday):',type(Weekday))
print('Weekday.Sun:',Weekday.Sun)
print('type(Weekday.Sun):',type(Weekday.Sun))

print('test.__members__:',test.__members__)
print('type(test):',type(test))

print('type(Enum):',type(Enum))
print('type(EnumMeta):',type(EnumMeta))

@unique
class Gender(Enum):
    Female = 0
    Male = 1

class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    @property
    def gender(self):
        return self.__gender
    def __str__(self):
        return self.__name+str(self.__gender)
    
    __repr__ = __str__

if __name__ == '__main__':
    bd = Student('BrilliantDawn',Gender.Male.value)
    print(bd)
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:#其实，枚举类的成员就是值，不一定非得盯着value=1看
        print('测试通过!')
    else:
        print('测试失败!')
