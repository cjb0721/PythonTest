"""
    生成器特点：节省内存 在遍历过程中生成对象 后续元素由前面元素计算不能使用索引
    1、列表生成器
"""
import sys
#
# list1 = [x for x in range(100000)]
# print(sys.getsizeof(list1), type(list1))
# print(list1[10])
#
# list2 = (x for x in range(100000))
# print(sys.getsizeof(list2), type(list2))
# # print(list2[10])  # 生成器不能再像列表那种使用下标的方式
#
# # for i in list2:
# #     if i<100:
# #         print(i)
# while True:
#     i = next(list2)
#     if i<100:
#         print(i)
#         print(list2.__next__())
#     else:
#         break
#
# list3 = (x for x in range(100))
# print(sys.getsizeof(list3), type(list3))



"""
    2、函数生成器
"""


def f():
    yield 1
    yield 2
    yield 3
    return "Hello"


# print(next(f()))
# print(next(f()))

# result = f()
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

result = f()
# try:
#     print(next(result))
#     print(next(result))
#     print(next(result))
#     print(next(result))
# except StopIteration as s:
#     print(s, "++++++++++")

for i in result:   # 遍历生成器的内容
    print(i)




