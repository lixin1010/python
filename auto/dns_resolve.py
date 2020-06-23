# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import dns.resolver
import os
import http.client

domain = input("input a domain: ")

cname = dns.resolver.query(domain, "A")

for i in cname.response.answer:
    for j in i.items:
        print(j.to_text())
# print(cname)
