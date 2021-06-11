#!/usr/bin/env python3
#-*- coding=utf-8 -*-

'''
学习廖雪峰教程@property注释

'''

__auther__='BrilliantDawn'

class Teacher(object):
    #__slots__ = ('name','sex','age')      #__slots__里的参数名要与__init__里一致，不然报冲突错误'name' in __slots__ conflicts with class variable

    __slots__ = ('__name','__sex','__age')

    def __init__(self,name,sex,age) -> None:
        self.__name = name
        self.__sex = sex
        self.__age = age
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise ValueError("name must be str!")
        self.__name = name

    @property
    def sex(self):
        return self.__sex


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise ValueError('age must be int!')
        if age<0 or age>130:
            raise  ValueError('age must be 0-130')
        self.__age = age    

class Screen(object):
    def __init__(self,width,height) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        if not isinstance(width,int):
            raise ValueError('width must be int')
        if width < 0:
            raise ValueError('width must be greater than 0')
        self.__width = width
    
    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self,height):
        if not isinstance(height,int):
            raise ValueError('height must be int')
        if height < 0:
            raise ValueError('height must be greater than 0')
        self.__height = height

    @property
    def resolution(self):
        return self.width*self.height

if __name__ == '__main__':
    t = Teacher('lc',1,28)
    print(t.name)
    print(t.age)
    print(t.sex)
    s = Screen(1280,720)
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
    #print('尝试修改性别')
    #t.sex = 0