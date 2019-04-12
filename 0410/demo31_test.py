import threading, time
import socket

# 构造客户端发送接收
#
# def send(client, addr):
#     while True:
#         # time.sleep(2)
#         # client.sendto("hello world".encode("utf8"), addr)
#         sendinfo = input("路人甲: ")
#         client.sendto(sendinfo.encode("utf-8"), addr)
#
#
# def receive(client, buff):
#     while True:
#         # time.sleep(3)
#         info, addr= client.recvfrom(buff)
#         print("info: ", info)
#         print("addr:", addr)
#
#
# if __name__ == '__main__':
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     ADDR_TO = ("127.0.0.1", 60001)
#     BUFFER_SIZE = 1024
#     client.sendto("hello world".encode("utf8"), ADDR_TO)
#     t1 = threading.Thread(target=send, args=(client, ADDR_TO, ))
#     t1.start()
#     t2 = threading.Thread(target=receive, args=(client, BUFFER_SIZE, ))
#     t2.start()
#     t1.join()
#     t2.join()


# 构造服务器端发送接收


def sever_send(sever):
    # time.sleep(10)
    while True:
        addr = int(input("请输入用户: "))
        info = input("请输入发送的内容: ")
        # sever.sendto(info.encode("utf8"), ("192.168.12.234", addr))
        sever.sendto(info.encode("GB2312"), ("192.168.12.234", addr))
        # return sever_receive(sever)


def sever_receive(sever):
    while True:
        info, addr = sever.recvfrom(1024)
        # print("info: ", info.decode("utf8"))
        # return sever_send(sever, result[1])
        print("addr: ", addr)
        print("收到用户 %d 发来的 %s" % (addr[1], info.decode("gb2312")))


if __name__ == '__main__':
    sever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ADDR_PORT = ("192.168.12.234", 60000)
    sever.bind(ADDR_PORT)
    # result = sever.recvfrom(1024)
    # print(result[1])
    t1 = threading.Thread(target=sever_send, args=(sever, ))
    t1.start()
    t2 = threading.Thread(target=sever_receive, args=(sever,))
    t2.start()
    t1.join()
    t2.join()











