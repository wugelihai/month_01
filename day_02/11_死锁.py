# 死锁，一直等待对方释放锁的情景就是死锁
# 根据下标在列表中取值
import threading
import time

# 创建互斥锁
mutex = threading.Lock()


def get_script(index):
    # 上锁
    mutex.acquire()

    my_list = [1, 4, 6, 8]
    if index >= len(my_list):
        print('下标越界：', index)
        # 释放锁，这里如果不解锁，直接会跳出这个函数，后面的解锁程序无法执行，就会形成死锁
        # 死锁代码会卡在那里，不会自动终止。
        mutex.release()
        return

    script = my_list[index]
    print(script)
    time.sleep(0.2)
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_script, args=(i,))
        sub_thread.start()


# 只要不是和计算密切相关的操作，那么就用多线程,进程和线程之间的优缺点要记住。

