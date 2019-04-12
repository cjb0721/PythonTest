import os, time
from multiprocessing import Pool


def process1(args1, args2, **kwds):
    time.sleep(1)
    print("process1 pid ", os.getpid(), args1, args2, kwds)


if __name__ == '__main__':
    print("main process pid ", os.getpid())
    # 构造进程池
    pool = Pool(4)
    for p in range(200):
        # 异步取进程池中的进程 非阻塞进程
        pool.apply_async(process1, args=(p,p), kwds={"num":p})
        # 同步取进程池中的进程 阻塞进程（第一个进程没有执行完毕，第二个进程不可用）
        # pool.apply(process1, args=(p,p), kwds={"num":p})
    # pool.apply_async(process1)
    time.sleep(5)
    # 终止进程池中所有进程
    pool.terminate()
    # 进程池不可用（进程照常运行）
    pool.close()
    # 阻塞主进程
    pool.join()
    print("finish")


