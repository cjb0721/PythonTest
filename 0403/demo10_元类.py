"""
    元类
"""


class Goods(object):
    pass


gd = Goods()
print(type(gd), type(Goods), type(type))


def getn(self):
    result = "hello"
    return result


# type元类：第一个参数: 类名；第二个参数: 父类；第三个参数: 类属性方法；
ai = type("AI", (), {"name": "ggb", "getn": getn})  # 使用type元类创建AI类
a1 = ai()  # 得到类实例

print(dir(ai))
print(dir(a1))

print(ai.__bases__)
print(ai.__class__)
print(a1.__class__)


def renameattr(classname, parrent, attr):
    # print(classname, parrent, attr)
    # print(classname.lower()[0])
    newattr = {}
    for k, v in attr.items():
        # print(k, v)
        if not k.startswith("__"):
            # print(k, v)
            k = classname.lower()[0] + "_" + k
            newattr[k] = v
    # print(newattr)
    return type(classname, parrent, newattr)


class Good(metaclass=renameattr):
    id = 110
    name = None


g = Good()
print(type(g))
print(dir(g))
print(Good.__bases__)
print(g.__dir__())
print(g.__getattribute__("g_id"))














