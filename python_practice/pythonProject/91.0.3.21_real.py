# _*_ coding: utf-8 _*_
__author__ = 'Li Xin'



import re
import csv
import codecs

file_csv = codecs.open('91.0.3.21.csv', 'wb', 'utf-8')
writer = csv.writer(file_csv, quoting=csv.QUOTE_MINIMAL)
Dev_Name = ['JL77RT0A-C1']
CSV_Title = ["Interface", "Status", "MAC Address", "IP Address"]
writer.writerow(Dev_Name)
writer.writerow(CSV_Title)
try:
    with open(r'dis_arp_91.0.3.21.txt', 'r') as file_arp:
        datas = file_arp.readlines()
    with open(r'91.0.3.21_arp.txt', 'w') as arp_txt:
        for data in datas:
            if not re.search('Incomplete', data) and not re.search('Eth-Trunk', data) and \
                    re.search(r'^91\.*\.*\.', data) and len(data.split()) > 4:
                data = data.split()
                InterfaceIndex = re.search(r'\d?/\d?/\d{1,2}', data[4]).group()
                info = 'GigabitEthernet' + InterfaceIndex + ',' + data[1] + ',' + data[0]
                arp_txt.write(info + '\n')
except Exception as e:
    print('Error:', e)
try:
    with open('int_bri.txt', 'r') as f:
        with open('deal_int_bri.txt', 'w') as fw:
            fr = f.readlines()
            fw.write('Interface,Status\n')
            for i in fr:
                if re.search(r'^GigabitEthernet\d?/\d?/\d{1,2}', i):
                    data = i.split()
                    fw.write(data[0] + ',' + data[1] + '\n')
except Exception as e:
    print('Error:', e)
file1 = open('91.0.3.21_arp.txt', 'r')
file2 = open('deal_int_bri.txt', 'r')
f1 = file1.readlines()
f2 = file2.readlines()
for i in f2:
    i = i.strip('\n').split(',')
    for j in f1:
        j = j.strip('\n').split(',')
        if i[0] == j[0]:
            xx = i[0] + ',' + i[1] + ',' + j[1] + ',' + j[2]
            xx = xx.split(',')
            writer.writerow(xx)

file1.close()
file2.close()