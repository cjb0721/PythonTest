import threading
import time


def thead1():
    lock1.acquire()
    time.sleep(1)
    lock2.acquire()
    print("thread1")


def thead2():
    lock2.acquire()
    time.sleep(2)
    lock1.acquire()
    print("thread2")


if __name__ == '__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    t1 = threading.Thread(target=thead1)
    t1.start()
    t2 = threading.Thread(target=thead2)
    t2.start()
    t1.join()
    t2.join()
    print("finish")


