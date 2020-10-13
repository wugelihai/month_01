import threading

# 0是不可变的数据类型，所以以下修改全局变量，全局变量的内存地址一直在发生变化,
# 多线程之间共享全局变量，容易形成多线程之间同一时刻取到同一变量。
# 说实话，这个有点打破结果的确定性
g_num = 0


def task1():
    # 修改全局变量
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    print(g_num)


def task2():
    # 修改全局变量
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    print(g_num)


if __name__ == '__main__':
    # 创建两个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    first_thread.start()
    # 设置等待，等上一个线程执行完成之后在执行下一个线程
    # first_thread.join()
    second_thread.start()
    # 查看全局变量修改的结果是否符合预期
    # print(g_num)


# 解决这种问题两种方式1.线程等待 join    2.互斥锁

