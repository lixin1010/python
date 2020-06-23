# _*_ coding: utf-8 _*_
__author__ = 'Li Xin'

import paramiko
from time import sleep
import sys
import re
import datetime
import time

class Brocade(object):
    def __init__(self, ip, username, password):
        self._ip = ip
        self._username = username
        self._password = password

    def connect(self, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self._ip, username=self._username, password=self._password)
        channel = ssh.invoke_shell()
        channel.settimeout(10)
        buff = ''
        channel.send(command + '\n')
        sleep(10)
        resp = channel.recv(65535)
        buff += bytes.decode(resp)
        #print(buff)
        if command == 'switchshow':
            with open(r'E:\学习\Python code\brocade\log\ ' + self._ip + '.txt', 'w') as f:
                f.write(buff)
        elif command == 'fabricshow':
            with open(r'E:\学习\Python code\brocade\log\fabricshow.txt', 'w') as f:
                f.write(buff)
        elif command == 'errdump':
            with open(r'E:\学习\Python code\brocade\log\log_' + self._ip + '.txt', 'w') as f:
                f.write(buff)

        channel.close()
        return

    def File_op(self):
        with open(r'E:\学习\Python code\brocade\log\fabricshow.txt', 'r') as f:
            fabric_info = f.readlines()
            L = []
            with open(r'E:\学习\Python code\brocade\log\fabric_info_ip.txt', 'w') as f_fabric_ip:
                with open(r'E:\学习\Python code\brocade\log\switch_ip.txt', 'a') as switch_ip:
                    for fabric_line in fabric_info:
                        fabric_cut = fabric_line.split()
                        # print(fabric_cut)
                        if len(fabric_cut) > 5:
                            pattern = '83|73\.[0-9]+\.[0-9]+\.[0-9]+'
                            if re.compile(pattern).search(fabric_cut[3]):
                                # print(type(i))
                                # d=re.compile(pattern).search(i)
                                L.append(fabric_cut[3])
                                switch_ip.write(fabric_cut[3]+'\n')
                                f_fabric_ip.write('Domain'+fabric_cut[0] + 'switch_ip' + fabric_cut[3] + 'switch_name' + fabric_cut[5] + '\n')
            print("This fabric has {} switches" .format(len(L)))

    def switch_count(self):
        with open(r'E:\学习\Python code\brocade\log\switch_ip.txt','r') as f:
            switch_count=f.readlines()
            print(len(switch_count))

def op_port():
    with open(r'E:\学习\Python code\brocade\log\switch_ip.txt', 'r') as f:
        for ip in f.readlines():
            with open(r'E:\学习\Python code\brocade\log\ ' + ip +'.txt', 'r') as fread:
                pass


def main():
    # Com_list = ['switchshow', 'fabricshow', 'errdump']
    Opt_1 = int(input("Choose command(0.show,1.checkport,2.update_fabric_info_ip)"))
    if Opt_1==0:
        # Seq = int(input("Choose command:(0.switchshow,1.fabricshow,2.errdump:)"))
        with open(r'E:\学习\Python code\brocade\log\switch_ip.txt', 'r') as f:
            #print(f.readlines())0
            for nums in f.readlines():
                # print(num)
                num=nums.strip("\n")
                Brocade_ssh = Brocade(num, username, password)
                Brocade_ssh.connect('switchshow')

        # ip_choose = input('Please input your switch IP:')
        # command = Com_list[Seq]
        # Brocade_ssh = Brocade(ip_choose, username, password)
        # Brocade_ssh.connect(command)
    elif Opt_1==1:
        pass

    elif Opt_1==2:
        # Opt_2=int(input("Choose Fabric(0.Fabric_A,1.Fabric_B):"))
        ip_list=["83.6.67.1","83.6.67.4"]
        for ip in ip_list:
            Brocade_ssh = Brocade(ip, username, password)
            Brocade_ssh.connect('fabricshow')
            Brocade_ssh.File_op()


if __name__ == '__main__':

    username = 'checklist'
    password = '3Aap24bJ'
    username_rw = 'fwauto'
    password_rw = 'Pass1234'
    nt=time.strftime("%Y%m%d")
    main()

# Brocade.connect()
