import json


class Good():
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price


with open("data.txt", "w") as f:
    g = Good("tea", 20)
    result = json.dumps(g.__dict__)  # 序列化 将对象类型的信息转换成str类型保存到文件中
    print(type(result))
    f.write(result)

with open("data.txt", "r") as f:
    result = f.read()
    print(type(result))
    g = json.loads(result)  # 反序列化 从文件中读到的信息通过loads方法转换成dict字典对象
    print(type(g), g)
