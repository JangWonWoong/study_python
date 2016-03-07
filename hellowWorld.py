# -*- coding: utf-8 -*-
#!/usr/bin/python
a = 5
b = 6
if (a + b) > 10:
    print("The sum is bigger than 10.")
import math
print(math.sqrt(25))

class Dog:
    def __init__(self, age=1):
        self.age = 1;
    def bark(self):
        print("Arf! Arf!")
    def sleep(self, minute=0,hour=0):
        print("I've slept {} hours(s) and {} minute(s)".format(hour,minute))

a_dog = Dog()
print(a_dog.age)
a_dog.bark()
a_dog.sleep(20)
a_dog.sleep(hour=1)
print(len("Wonwoong Jang"))

# 단일 주석
'''
    멀티 라인 주석
'''
"""
    멀티 라인 주석
"""