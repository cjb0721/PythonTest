"""
    闭包：
    1、函数内部声明函数
    2、外部函数返回内部函数的引用
    3、内部函数可以访问外部函数的局部变量
"""


def fun1(a):
    def fun2(b):
        nonlocal a  # 使用nonlocal标识a不是内部函数的变量
        a += 1
        return a+b
    return fun2


f = fun1(10)
print(f(20))
print(f(20))


# import demo06_装饰器 as d
# d.show_list()

from demo06_装饰器 import show_list
show_list()

