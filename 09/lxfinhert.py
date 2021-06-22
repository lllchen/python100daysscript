#!/usr/bin/env python3
#-*- encoding=utf-8 -*-

'''
廖雪峰多继承练习通常称之为MixIn

'''

__auther__='BrilliantDawn'


class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(Animal):
    def sport(self):
        return 'I am running!'
    pass

class Flyable(Animal):
    def sport(self):
        return 'I am flying...'
    pass

class Dog(Mammal,Runnable):
    pass

class Ostrich(Bird,Runnable):
    pass

class Parrot(Bird,Flyable):
    pass

class Bat(Mammal,Flyable):
    pass


def main():
    dog = Dog()
    ostrich = Ostrich()
    parrot = Parrot()
    bat = Bat()
    print('dog is sport:',dog.sport())
    print('ostrich is sport:',ostrich.sport())
    print('parrot is sport:',parrot.sport())
    print('bat is sport',bat.sport())


if __name__=='__main__':
    main()