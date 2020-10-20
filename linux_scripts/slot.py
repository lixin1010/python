# _*_ coding:utf-8 _*_
# /usr/bin/python3
class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
print(s.name)
s1 = Student()
s1.age = 34
