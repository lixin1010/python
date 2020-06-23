import time
from time import sleep

__author__ = 'Li Xin'

Lyric = open("hero", "r", encoding="utf-8")
#print(Lyric)
count = 1
for line in Lyric:
    if count == 10:
        break
    print(line)
    count += 1

"""
while True:

    data = Lyric.readline()
    print(data.strip())
    sleep(1)
    if not data:
        break
"""