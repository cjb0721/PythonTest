from multiprocessing import Process


class MyProcess(Process):
    # def __init__(self):
    #     Process.__init__(self)

    def run(self):
        print("重写run方法执行...")


def fun1():
    print("进程1执行")


def main():
    # p1 = MyProcess(target=fun1)
    p1 = MyProcess()
    p1.start()

if __name__ == '__main__':
    main()

