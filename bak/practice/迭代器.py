# -*- coding:utf-8 -*-
__author__ = 'Li Xin'
from time import sleep
with open('/Users/lixin/1.txt', 'r') as f:
    for i in f:
        print(i)
        sleep(2)
