"""
    引用计数
"""

from sys import getrefcount

list1 = [x for x in range(10)]
list2 = [x for x in range(10, 20)]

print(list1)
print(list2)
print("=========================================")

print(getrefcount(list1))
print(getrefcount(list2))
print("=========================================")

list1.append(list2)
print(list1)
print(getrefcount(list1))
print(getrefcount(list2))
print("=========================================")

list2.append(list1)
print(list2)
print(getrefcount(list1))
print(getrefcount(list2))
print("=========================================")

del list1
print(list2)
print(getrefcount(list2))
print("=========================================")