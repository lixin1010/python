# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import dns.resolver
import os
import http.client

iplist = []
appdomain = "www.google.com"


def get_iplist(domain=""):
    try:
        A = dns.resolver.resolve(domain, 'A')
    except Exception as e:
        print("dns resolver error" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
            #print(iplist)
    return True
        #print(iplist)


def checkip(ip):
    checkurl = ip + ":443"
    getcontent = ""
    #http.client.
    conn = http.client.HTTPSConnection(checkurl)

    try:
        conn.request("get", "/", headers={"Host": appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)
    finally:
        if getcontent == "<!doctype html>":
            print(ip + '[OK]')
        else:
            print(ip + '[ERROR]')


if __name__ == "__main__":
    #print(get_iplist(appdomain))
    if get_iplist(appdomain) and len(iplist):
        for ip in iplist:
            checkip(ip)
    else:
        #print(len(iplist))
        print("dns resolver error")
