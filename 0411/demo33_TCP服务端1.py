# 1、引入模块
from socket import *
# 2、构造服务端对象
sever = socket(AF_INET, SOCK_STREAM)
# 3、绑定地址
SEVER_ADDR = ("192.168.12.234", 6666)
sever.bind(SEVER_ADDR)
# 4、开始监听
sever.listen()
print("开启监听")
# 5、接受连接
# result = sever.accept()
# print(result)
client, client_addr = sever.accept()
print(client_addr)
# print(client)
# 6、接受消息
BUFFER_SIZE = 1024
info = client.recv(BUFFER_SIZE)
print(info.decode("gb2312"))
# 7、发送消息
input_str = input("请输入发送信息: ").encode("gb2312")
client.send(input_str)

client.close()
sever.close()
