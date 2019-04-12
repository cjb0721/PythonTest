from socket import *
import threading


# TCP服务端接收和发送
def trecv(client):
    while True:
        BUFFER_SIZE = 1024
        info = client.recv(BUFFER_SIZE)
        if len(info) > 0:
            lists = info.decode("gbk").split(":")
            up = lists[0]
            um = lists[1].encode("gbk")
            if up in user.keys():
                user[up].send(um)
            else:
                client.send("对方已离线，不能发送消息".encode("gbk"))
            # print("接收来自用户", client.getpeername()[1], "发来的消息: ", info.decode("gb2312"))
        else:
            user.pop(str(client.getpeername()[1]))
            print("当前在线人数: ", len(user))
            break


# def tsend(client):
#     while True:
#         str_in = input("请输入发送消息: ").encode("gb2312")
#         result = client.send(str_in)
#         # print(type(result), result)
#         if result:
#             print("发送成功")


def tlisten():
    while True:
        client, client_addr = sever.accept()
        user[str(client_addr[1])] = client
        print("用户", client_addr, "上线了. 当前在线用户人数", len(user))
        t2 = threading.Thread(target=trecv, args=(client, ))
        t2.start()


if __name__ == '__main__':
    user = {}
    sever = socket(AF_INET, SOCK_STREAM)
    SEVER_ADDR = ("192.168.12.234", 8888)
    sever.bind(SEVER_ADDR)
    sever.listen()
    print("启动监听")
    t1 = threading.Thread(target=tlisten, )
    t1.start()

    # client, client_addr = sever.accept()
    # t1 = threading.Thread(target=trecv, args=(client, client_addr))
    # t1.start()
    # t2 = threading.Thread(target=tsend, args=(client, ))
    # t2.start()
    # t1.join()
    # t2.join()
    # client.close()
    # sever.close()


# TCP客户端接收发送消息
# def tsend(client):
#     while True:
#         try:
#             if client._closed:
#                 break
#             else:
#                 str_in = input("请输入发送的内容: ")
#                 if client._closed:
#                     break
#                 else:
#                     client.send(str_in.encode("gb2312"))
#                     print("发送成功")
#         except Exception as e:
#             print(e)
#
#
# def trecv(client):
#     BUFFER_SIZE = 1024
#     while True:
#         try:
#             info = client.recv(BUFFER_SIZE).decode("gb2312")
#             if len(info) > 0:
#                 print(info)
#             else:
#                 client.close()
#                 break
#         except Exception as e:
#             print(e)
#
#
# if __name__ == '__main__':
#     try:
#         client = socket(AF_INET, SOCK_STREAM)
#         SEVER_ADDR = ("192.168.12.234", 60000)
#         client.connect(SEVER_ADDR)
#
#         t1 = threading.Thread(target=trecv, args=(client,))
#         t1.start()
#         t2 = threading.Thread(target=tsend, args=(client,))
#         t2.start()
#         t1.join()
#         t2.join()
#         client.close()
#         print("连接断开")
#     except Exception as e:
#         print(e)









