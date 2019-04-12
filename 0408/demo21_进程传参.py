from multiprocessing import Process
import time


def mainprocess(pam1, pam2, **kwargs):
    print(pam1, pam2, kwargs)
    pam1.append(2)
    print(pam1, pam2, kwargs)


def main():
    list1 = [1]
    p1 = Process(target=mainprocess, args=(list1, list1), kwargs={"name":"ggb", "age":18})
    p1.start()
    time.sleep(1)
    print(list1)


if __name__ == '__main__':
    main()
