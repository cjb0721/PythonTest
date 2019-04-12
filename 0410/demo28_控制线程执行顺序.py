import threading


def thread1():
    lock1.acquire()
    print("thread1")
    lock1.release()


def thread2():
    lock2.acquire()
    print("thread2")
    lock1.release()


def thread3():
    lock3.acquire()
    print("thread3")
    lock2.release()


if __name__ == '__main__':
    lock1 = threading.Lock()
    lock1.acquire()
    lock2 = threading.Lock()
    lock2.acquire()
    lock3 = threading.Lock()
    # lock3.acquire()

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t3 = threading.Thread(target=thread3)
    t1.start()
    t2.start()
    t3.start()
    print("END")

