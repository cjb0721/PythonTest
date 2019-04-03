"""
    类装饰器
"""


class Check():

    def __init__(self, _fun):
        print("执行构造方法初始化")
        self.f = _fun

    def __call__(self, *args, **kwargs):
        print("执行call方法")
        self.f()


@Check
def login():
    print("执行原始函数")


# "使用实例名（）会执行类内部call方法"
# ch = Check()
# ch()


login()
