import threading
# 使用互斥锁解决全局变量数据错误问题，当一个线程使用全局变量时会上锁，用好之后在开锁，然后大家在一起抢

g_num = 0

# 创建锁,本质上是一个函数Lock,调用函数得到一把锁
mutex = threading.Lock()    # mutex  互斥锁


def task1():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    print(g_num)
    # 释放锁
    mutex.release()


def task2():
    # 上锁
    mutex.acquire()  # 收获，捕获
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    print(g_num)
    # 释放锁
    mutex.release()  # 释放


if __name__ == '__main__':
    # 创建两个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    first_thread.start()
    second_thread.start()

# 互斥锁，哪个线程抢到锁，不是我们可以决定的，线程执行完成之后就会销毁
# 互斥锁解决问题方式比较简单，但是性能会有所降低，一个时间只能有一个线程来执行。
# 火车买票的形式可以理解为互斥锁，保证数据的准确性
# 要上锁都上锁，如果一个上锁，一个不上锁，那就没啥用，因为不上锁的数据不遵守互斥锁规则
