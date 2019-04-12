from socket import *
import threading


def trecv(client, nickname):
    while True:
        result = client.recv(1024)
        if len(result) > 0:
            info = result.decode("gbk").split(":")
            to = info[0]
            mess = info[1]
            print(to, mess)
            if to == "all":
                for k in user.keys():
                    if nickname != k:
                        user[k].send((nickname+":"+mess).encode("gbk"))
            else:
                if to in user.keys():
                    user[to].send((nickname+":"+mess).encode("gbk"))
                else:
                    client.send("对方已离线，不能接收消息".encode("gbk"))
        else:
            client.close()
            user.pop(nickname)
            break


def tlisten(sever):
    while True:
        client, client_addr = sever.accept()
        nickname = client.recv(1024).decode("gbk")
        user[nickname] = client
        print("用户", nickname, "上线了。 当前在线人数", len(user))
        t2 = threading.Thread(target=trecv, args=(client, nickname))
        t2.start()


# def tsend(sever):
#     while True:
#         info = input("请输入通知: ").encode("gbk")
#         for u in user.keys():
#             user[u].send(info)


if __name__ == '__main__':
    user = {}

    sever = socket(AF_INET, SOCK_STREAM)
    sever.bind(("192.168.12.234", 8888))
    sever.listen(20)
    print("开启监听")
    t1 = threading.Thread(target=tlisten, args=(sever,))
    t1.start()

    # t3 = threading.Thread(target=tsend, args=(sever, ))
    # t3.start()


