from socket import *
import threading


# TCP服务端接收和发送
def trecv(client, method):
    while True:
        try:
            BUFFER_SIZE = 1024
            if method == 1:
                info = client.recv(BUFFER_SIZE)
                if len(info) > 0:
                    lists = info.decode("gbk").split(":")
                    up = lists[0]
                    um = lists[1].encode("gbk")
                    if up in user.keys():
                        user[up].send(um)
                    else:
                        client.send("对方已离线，不能发送消息".encode("gbk"))
                else:
                    user.pop(str(client.getpeername()[1]))
                    print("当前在线人数: ", len(user))
                    break
            elif method == 2:
                info = client.recv(BUFFER_SIZE)
                if len(info) > 0:
                    mess = info.decode("gbk")
                    # temp = user.pop(str(client.getpeername()[1]))
                    # print(type(temp), temp)
                    if len(user) > 1:
                        self_port = str(client.getpeername()[1])
                        # print(self_port, type(self_port))
                        for k, v in user.items():
                            if k == self_port:
                                continue
                            else:
                                # print("======>", k, type(k))
                                user[k].send(mess.encode("gbk"))
                            # print(k, v)
                    else:
                        client.send("当前无人在线，不能发送消息".encode("gbk"))

                else:
                    user.pop(str(client.getpeername()[1]))
                    print("当前在线人数: ", len(user))
                    break
        except Exception as e:
            print(e)


def fun1(x, y):
    return (x, y)


def tlisten():
    while True:
        try:
            nickname = input("请输入昵称: ")
            list1.append(nickname)
            client, client_addr = sever.accept()
            user[str(client_addr[1])] = client
            result = map(fun1, list1, user)
            # print(type(result),result)
            # for r in result:
            #     print(r)
            print("用户", client_addr, "上线了. 当前在线用户人数", len(user))
            print("* ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *")
            print("发送类型: 1、私聊  2、所有人")
            method = int(input("请选择发送类型: "))
            if 0 < method < 3:
                t2 = threading.Thread(target=trecv, args=(client, method))
                t2.start()
            else:
                print("输入有误， 请重新开启连接！")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        user = {}
        list1 = []
        sever = socket(AF_INET, SOCK_STREAM)
        SEVER_ADDR = ("192.168.12.234", 6666)
        sever.bind(SEVER_ADDR)
        sever.listen()
        print("启动监听")
        t1 = threading.Thread(target=tlisten, )
        t1.start()
        t1.join()
        sever.close()
    except Exception as e:
        print(e)











