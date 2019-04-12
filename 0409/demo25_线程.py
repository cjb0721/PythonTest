import time, threading
from threading import Thread


def time_count(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, end-start)
    return fun


def time_thread():
    print("++")
    time.sleep(1)


@time_count
def main():
    for i in range(5):
        print("++")
        time.sleep(1)


@time_count
def thread_main():
    list_thread = []
    for t in range(5):
        t = Thread(target=time_thread)
        t.start()
        list_thread.append(t)
    for l in list_thread:
        l.join()


if __name__ == '__main__':
    # main()
    thread_main()


