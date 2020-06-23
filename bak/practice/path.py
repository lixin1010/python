# -*- coding:utf-8 -*-
__author__ = 'Li Xin'
import os
import sys

print(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)

import SSH


