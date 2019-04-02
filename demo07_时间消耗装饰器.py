import datetime, time


def timecount(fun):
    def tc():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, "消耗:", end - start)
    return tc

@timecount
def fun1():
    list1 = [x for x in range(100000)]
    print(list1.index(99999))


@timecount
def fun2():
    list2 = (x for x in range(100000))
    count = 0
    while True:
        try:
            result = next(list2)
            if result == 99999:
                print(count)
                break
            count += 1
        except StopIteration as s:
            print(s, "end")


fun1()
fun2()
