import copy

# “=”一般意义的复制
# list1 = [1, 2, 3, [4, 5]]
# list2 = list1
# print(list2 is list1)
# print(list2[3] is list1[3])
# list1[3].insert(1, 4.5)
# list2.insert(3, 3.5)
# print(list1, list2)

# 浅拷贝 外层拷贝值 内层拷贝引用
# list1 = [1, 2, 3, [4, 5]]
# list2 = copy.copy(list1)
# print(list2 is list1)
# print(list2[3] is list1[3])
# list1[3].insert(1, 4.5)
# list2.insert(3, 3.5)
# print(list1, list2)

# 深拷贝 内外层都只拷贝值
list1 = [1, 2, 3, [4, 5]]
list2 = copy.deepcopy(list1)
print(list2 is list1)
print(list2[3] is list1[3])
list1[3].insert(1, 4.5)
list2.insert(3, 3.5)
print(list1, list2)
