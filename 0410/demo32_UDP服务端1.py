# 1、引入socket模块
from socket import *
# 2、构造服务端socket对象
server = socket(AF_INET, SOCK_DGRAM)
# 3、绑定地址
server.bind( ("192.168.12.234", 60002) )

result = server.recvfrom(1024)
print(result)

info = input("路人甲: ")
server.sendto(info.encode("utf8"), result[1])

