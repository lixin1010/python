# -*- coding:utf-8 -*-
__author__ = 'Li Xin'
import time
x = time.localtime()
time.strftime("%Y-%m-%d %X",x)
print(time.strftime("%X",x))

print(time.strptime('2019-12-18 20:00:49',"%Y-%m-%d %X"))

print(time.asctime())
# print(x)

print(time.ctime())

