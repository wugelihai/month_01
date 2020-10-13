import multiprocessing
import time


def test():
    for i in range(10):
        print('任务执行中。。。')
        time.sleep(0.3)


# 从这里就可以看出，主进程要等所有子进程执行结束后才会退出程序
if __name__ == '__main__':
    test_process = multiprocessing.Process(target=test)
    test_process.start()
    # 把子进程设置为守护进程
    # test_process.daemon = True
    time.sleep(0.5)
    # 主进程推出之前先销毁子进程

    print('over')

    test_process.terminate()
    print('我的')

# 那么想让子进程随着主进程一起结束该怎么办呢？
# 两种方法：1.把子进程设置为守护主进程，主进程结束后子进程也会结束，在启动子进程下加上   子进程.daemon = True
# 2. 主进程退出之前，先销毁子进程   在主进程前加上  主进程.terminate()
