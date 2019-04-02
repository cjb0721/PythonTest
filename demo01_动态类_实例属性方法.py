"""
    Python动态语言
"""
import types


class AI(object):
    "这是一个AI类"
    __slots__ = ('hp', 'mp', 'move')  # 限制添加的内容属性

    def __init__(self, _hp):
        self.hp = _hp


a1 = AI(50)
print(a1.hp)


# 1、动态添加类属性
AI.isalive = False  # 通过类名动态添加类属性
print(AI.isalive)
print(a1.isalive)  # 实例也拥有该动态类属性

# 2、动态添加实例属性
a1.mp = 80
print(a1.mp)


# 3、动态添加实例方法
def move(self):  # 定义实例方法
    print("move")


a2 = AI(50)
a2.move = types.MethodType(move, a2)
a2.move()


# 4、动态添加类方法、静态方法
@classmethod
def attack(cls):  # 定义类方法
    print("attack")


@staticmethod
def dead():  # 定义静态方法
    print("dead")


a3 = AI(50)
AI.attack = attack
AI.attack()
AI.dead = dead
AI.dead()

# 5、动态删除属性、方法
del a2.move
if hasattr(a2, "move"):
    print("存在move方法")
else:
    print("不存在move方法")

# delattr(AI, "move")
# if hasattr(a2, "move"):
#     print("存在move方法")
# else:
#     print("不存在move方法")

# a2.move()
print(AI.__doc__)
