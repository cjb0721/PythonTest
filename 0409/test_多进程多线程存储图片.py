import requests, re, os, threading
from multiprocessing import Pool
import demo25_线程 as t


# 单进程单线程
@t.time_count
def main():
    print(" process pid: ", os.getpid())
    with open("data.txt", "r") as f:
        result = f.read()
        list1 = re.findall(r'(.*?).jpg', result)
        num = 0
        # print(list1)
        list2 = list(set(list1))
        list2.sort(key=list1.index)
        # print(list2)
        for l in list2:
            response = requests.get(l+".jpg")
            # print(response.content)
            # print(l.split("/")[-1])
            with open("img/"+l.split("/")[-1]+".jpg", "wb") as f:
                try:
                    f.write(response.content)
                    print("成功写入"+l.split("/")[-1]+".jpg")
                except:
                    print("写入错误")
            num += 1


def write(response, path):
    with open("img/"+path.split("/")[-1]+".jpg", "wb") as f:
        try:
            f.write(response.content)
            print("成功写入"+path.split("/")[-1]+".jpg")
        except:
            print("写入错误")


# 多线程
@t.time_count
def thread_main():
    with open("data.txt", "r") as f:
        result = f.read()
        list1 = re.findall(r'(.*?).jpg', result)
        list2 = []
        for t in list1:
            response = requests.get(t+".jpg")
            # print(t.split("/")[-1])
            t1 = threading.Thread(target=write, args=(response, t))
            t1.start()
            list2.append(t1)
        for l in list2:
            l.join()


# 多进程
@t.time_count
def pool_main():
    pool = Pool(4)
    with open("data.txt", "r") as f:
        result = f.read()
        list1 = re.findall(r'(.*?).jpg', result)
        for t in list1:
            response = requests.get(t + ".jpg")
            pool.apply_async(write, args=(response, t))
        pool.close()
        pool.join()


if __name__ == '__main__':
    main()
    # thread_main()
    # pool_main()
