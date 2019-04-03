"""
类 与对象（实例）
类：模板定义属性和方法的封装
实例：具体的类对象 ，类的表现

1实例属性会根据实例不同而不同，类属性由类决定
2实例属性通常在构造赋值
3类属性（类变量）属于类 ， 实例属性属于实例
实例确定，实例属性确定
实例可以调用类属性  ，类不可以调用实例属性
"""

class Good():
    name = 'tea'

    def __init__(self, _addr):
        self.addr = _addr

g1 = Good("fujian")
g2 = Good("guangdong")

print(g1.addr,g2.addr,g1.name,g2.name)
Good.name = 'coffee'
print(Good.name, g1.name)

# print(id(g1), id(g2))
# print(id(g1.name), id(g2.name), id(Good.name))

# 给g1对象添加name 属性
g1.name = 'cookle'

print(id(g1.name), id(g2.name), id(Good.name))




"""
实例方法：需要第一个参数为self
类方法：需要第一个参数为cls,并且使用@classmethod声明
静态方法:需要使用@staticmethod声明

类可以调用，类方法， 静态方法
实例可以调用, 类方法，静态方法，实例方法

"""
class Good():
    """
    这是一个商品类
    """
    def __init__(self,_name):
        self.name = _name

    def getname(self):
        return self.name

    @classmethod
    def getinfo(cls):
        print(cls.__doc__)


    @staticmethod
    def pprint():
        print("hellogood")

g1 = Good("tea")
print(g1.getname())
g1.getinfo()
g1.pprint()

# Good.getname()
Good.getinfo()
Good.pprint()




"""
类属性类方法
类属性类方法 属于类 只占一份内存
实例方法，实例属性属于实例 每使用一个实例生成一个内存
声明实例属性，实例方法 浪费内存，适当的选择声明类属性和类方法节省内存

"""

class Util():
    @staticmethod
    def max(x,y):
        if x>y:
            return x
        else:
            return y




"""
属性编写
"""
class Good():
    def __init__(self,_name):
        self.name = _name

    @property
    def gname(self):
        return self.name

    @gname.setter
    def gname(self,_name):
        self.name = _name

g1 = Good("tea")
print(g1.name)
g1.gname = "coffee"
print(g1.gname)
"调用形式  没有赋值就是获取  赋值就是设置"



