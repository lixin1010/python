list_1 = [1,4,5,6,7,8,2,0,8,5]
list_1 = set(list_1)
print(list_1, type(list_1))

list_2 = set([2, 55, 6, 8, 10])
print(list_1.intersection(list_2))
#交集
print(list_2.union(list_1))
#并集

print(list_1.difference(list_2))
#差集
