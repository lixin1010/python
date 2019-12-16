# -*- coding:utf-8 -*-
__author__ = 'Li Xin'
import sys
import paramiko


class SSHtoServer(object):
    def __init__(self):
        self.IpAddress = '39.100.238.239'
        self.port = 22
        self.username = 'root'
        self.password = 'LI10yang15'
        self.__k = None

    def run(self):
        self.connect()
        self.command()
        self.close()

    def connect(self):
        transport = paramiko.Transport(self.IpAddress, self.port)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        transport.connect(username=self.username, password=self.password)
        self.__transport = transport

    def command(self):
        ssh = paramiko.SSHClient()
        cmd = 'cd /etc/ ; ls -l'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # result = stdout.read()
        # print(result)

    def close(self):
        self.__transport.close()
    # def download(self):
    #    sftp = paramiko.SFTPClient.from_transport(self.__transport)
    #    sftp.get()


ssh1 = SSHtoServer()
ssh1.run()
