"""
    迭代器(Iterator): 可以使用next方法 (eg: 生成器既是迭代器又是可迭代)
    可迭代(Iterable): 可使用for循环遍历 (eg: list、dict、set、trouble、str)
    iter(): 可以将可迭代对象转换成迭代器
"""

from collections.abc import Iterable, Iterator

# list1 = [1, 2, 3]
# print(isinstance(list1, Iterator))
# print(isinstance(list1, Iterable))
#
# dict1 = {"name":"ggb", "age":18}
# print(isinstance(dict1, Iterator))
# print(isinstance(dict1, Iterable))
#
# list1iter = iter(list1)
# print(next(list1iter), isinstance(list1iter, Iterator))
# print(next(list1iter), isinstance(list1iter, Iterator))


class Goods():

    def __init__(self, _addr, _index):
        self.addr = _addr
        self.index = _index

    # iter方法标识是迭代器不能省；否则就只是普通遍历,是可迭代但不是迭代器
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.addr):
            res = self.addr[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration


l = ["河南省", "郑州市", "金水区"]
g = Goods(l, 0)

print(isinstance(g, Iterator))
print(isinstance(g, Iterable))

print(isinstance(Goods, Iterator))
print(isinstance(Goods, Iterable))

try:
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
except StopIteration as s:
    print(s, "+++++++")

print("end")


