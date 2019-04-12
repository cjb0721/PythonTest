# 客户端
from socket import *
import threading


def tsend(client):
    while True:
        to = input("请输入接收用户: ")
        mess = input("请输入发送消息: ")
        if not client._closed:
            client.send((to+":"+mess).encode("gbk"))
        else:
            print("离线中...")
            break


def trecv(client):
    try:
        while True:
            result = client.recv(1024)
            if len(result) > 0:
                info = result.decode("gbk").split(":")
                mess_from = info[0]
                mess_detail = info[1]
                print(mess_from, mess_detail)
            else:
                client.close()
                break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("192.168.12.234", 8888))
    nickname = input("请输入昵称: ").encode("gbk")
    client.send(nickname)
    t1 = threading.Thread(target=trecv, args=(client,))
    t1.start()
    t2 = threading.Thread(target=tsend, args=(client,))
    t2.start()
    t1.join()
    t2.join()