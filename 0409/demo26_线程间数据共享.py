import threading, time


def thread1():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()


def thread2(pam1):
    time.sleep(1)
    print(pam1, threading.current_thread().name, threading.currentThread().is_alive())


def main():
    list1 = [1, 2, 3]
    for t in range(5):
        t1 = threading.Thread(target=thread2, args=(list1,), name="MyThread"+str(t))
        t1.start()
        t1.join()


if __name__ == '__main__':
    num = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=thread1)
    t1.start()
    t2 = threading.Thread(target=thread1)
    t2.start()
    t1.join()
    t2.join()
    print(num)

    main()
    print("finish")


