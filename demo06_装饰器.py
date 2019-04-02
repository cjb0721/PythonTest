"""
    装饰器
"""


def fun1(msg):
    def fun2():
        result = input("请输入用户名: ")
        if result == 'ggb':
            msg()
        else:
            print("权限不足")
    return fun2


@fun1
def show_list():
    list1 = [x for x in range(10)]
    print(list1)


show_list()
