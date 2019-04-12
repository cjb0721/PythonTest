import os, time
from multiprocessing import Process


def fun1():
    time.sleep(2)
    print("进程1执行")


def fun2():
    while True:
        print("进程2执行")
        time.sleep(1)

    
def main():
    p1 = Process(target=fun1)
    p1.start()
    # p1.join()
    p2 = Process(target=fun2)
    p2.start()
    print(p1.pid, p2.pid)
    while True:
        pause = p1.is_alive()
        print(p1.is_alive(), p2.is_alive())
        if not pause:
            print("进程1结束")
            p2.terminate()
            print("进程2终止")
            break
        else:
            time.sleep(1)


if __name__ == '__main__':
    main()
    


