from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(("192.168.12.234", 60000))

str_in = input("请输入发送信息: ").encode("gb2312")
client.send(str_in)
print("发送成功")

while True:
    result = client.recv(1024).decode("gb2312")
    if len(result) > 0:
        print(result)
    else:
        break
client.close()
