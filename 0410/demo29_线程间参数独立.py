import threading


def thread1():
    local_var.name = "ggb"
    print(local_var.name)


def thread2():
    local_var.age = 18
    print(local_var.age)


if __name__ == '__main__':
    local_var = threading.local()
    # print(local_var, type(local_var))

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # print(local_var.name)
    # print(local_var.age)

