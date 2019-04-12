"""
    map: 将两个可迭代内容进行映射
    reduce: 将序列化中的数值进行累计
"""


def fun1(x, y):
    return (x, chr(y))


def fun2(x):
    if x%2 == 0:
        return x


def fun3(x, y):
    return x+y


list1 = [x for x in range(1, 10)]
list2 = [y for y in range(ord('a'), ord('z'))]
result1 = map(fun1, list1, list2)
print(type(result1))
for i in result1:
    print(i)

result2 = filter(fun2, list1)
print(type(result2))
for i in result2:
    print(i)

from _functools import reduce
sum1 = reduce(fun3, list1)
print(sum1)

