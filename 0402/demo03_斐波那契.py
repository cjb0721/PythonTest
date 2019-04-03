def feibo(num):
    a, b = 0, 1
    yield a
    yield b

    count = 0
    while count < num:
        a, b = b, a + b          
        yield b       # 1 2
        count += 1


result = feibo(5)
for i in result:
    print(i)

# 青蛙爬楼梯一次跳1/2阶，共几种跳法：[1, 2, 3, 5, 8, 13, 21, 34, 55 , ...]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 , ...]
