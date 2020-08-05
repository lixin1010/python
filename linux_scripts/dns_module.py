# -*- coding:utf-8 -*-
__author__ = 'Li Xin'

import dns.resolver

domain = input("a domain:")
A = dns.resolver.resolve(domain, "A")
for i in A.response.answer:
    for j in i.items:
        print(j.address)

domain = input("another domain:")
Cn = dns.resolver.resolve(domain, 'CNAME')
for i in Cn.response.answer:
    for j in i.items:
        print(j.to_text())
