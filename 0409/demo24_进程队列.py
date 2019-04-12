import os, time
from multiprocessing import Process, Queue


def pwrite(queue):
    for q in range(10):
        time.sleep(1)
        queue.put(q)
        print(queue.qsize())


def pdo(res):
    print("执行任务: ", res)


def pread(queue):
    while True:
        if queue.qsize() == 0:
            break
        result = queue.get()
        print("读取到任务: ", result)
        pdos = Process(target=pdo, args=(result,))
        pdos.start()


if __name__ == '__main__':
    queue = Queue(10)
    pw = Process(target=pwrite, args=(queue, ))
    pw.start()
    print("pw pid: ", pw.pid)
    pw.join()

    pr = Process(target=pread, args=(queue, ))
    pr.start()
    print("pr pid: ", pr.pid)
    pr.join()
    print("finish")






