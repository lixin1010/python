# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import psutil

mem = psutil.virtual_memory()

print(mem.total, mem.used)
