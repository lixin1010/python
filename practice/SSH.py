# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import paramiko
import time


class SSHtoSERVER(object):
    def __init__(self):
        self.IpAddress = '39.100.238.239'
        self.port = 22
        self.username = 'root'
        self.password = 'LI10yang15'
        # self.__k = None

    def run(self):
        self.connect()
        self.command()
        self.sftp_download()
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.IpAddress, self.port))
        transport.connect(username=self.username, password=self.password)
        self._transport = transport

    def command(self):
        ssh = paramiko.SSHClient()
        cmd = 'ps -aux >/var/log1031.txt\n'
        ssh._transport = self._transport  # 啥意思----相当于登录动作
        ssh.exec_command(cmd)
        # result = stdout.read()
        # print(result)

    def sftp_download(self):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.get('/var/log1031.txt', '/Users/lixin/1.txt')
        sftp.put('/users/lixin/1.txt', '/var/1.txt')

    def close(self):
        self._transport.close()


test = SSHtoSERVER()
n = 1
while n:
    test.run()
    time.sleep(3)
    n = n-1
