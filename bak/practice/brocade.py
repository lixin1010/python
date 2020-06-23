# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import paramiko
from time import sleep

blip = '83.7.67.100'
bluser = 'checklist'
blpasswd = '3Aap24bJ'
# hostIP = '83.6.67.113'
username = 'rw001160180'
password = '2swd1tpu'
cmd = "switchshow"
disable = 'Disabled'
# portMgr = 'portcfgpersistentenable'
with open('switchIP.txt', 'r') as f:
    for hostIP in f:
        ssh_login = 'ssh -l ' + username + " " + hostIP
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=blip, username=bluser, password=blpasswd)
        channel = ssh.invoke_shell()
        channel.settimeout(10)
        buff = ''
        channel.send(ssh_login + '\n')
        channel.send(password + '\n')
        sleep(3)
        channel.send(cmd + '\n')
        sleep(12)
        resp = channel.recv(65535)
        buff += bytes.decode(resp)
        if ('BS65' or 'BS53' or 'BS49') in buff:
            with open('switch.txt', 'w') as f:
                f.write(buff)
            with open('switch.txt', 'r') as readf:
                for i in readf:
                    if disable in i:
                        with open('disable.txt', 'a+') as f:
                            f.write(i)
                        # j=i.strip()[:2]
                        # print(j[:2])
                        # print(j)
                        # channel.send(portMgr+' '+j+'\n')
                        # sleep(3)
                        # resp1 = channel.recv(65535)
                        # buff1 = ''
                        # buff1 += bytes.decode(resp1)
                        # print(buff1)
        elif ('BS85' or 'BSDX' or 'BS48') in buff:
            with open('switch.txt', 'w') as f:
                f.write(buff)
            with open('switch.txt', 'r') as readf:
                for i in readf:
                    if disable in i:
                        with open('disable.txt', 'a+') as f:
                            f.write(i)
                        j = i.split()  # 将每行元素形成一个列表
                        print(j[1] + '/' + j[2])
                        # print(j[1],j[2])

        channel.close()
        ssh.close()
