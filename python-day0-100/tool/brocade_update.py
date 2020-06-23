# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import sys
import paramiko


class Brocade:
    def __init__(self, ip, username, password):
        self._ip = ip
        self._username = username
        self._password = password

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self._ip, username=self._username, password=self._password)

    def switchshow(self):
        try:
            channel = ssh.invo



if __name__ == '__main__':
    ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    Brocade(ip, username, password)
