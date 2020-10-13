import threading 
import time

add_num = []


def unord():
    time.sleep(0.2)
    for i in range(5):
        add_num.append(i)
        print('add_num:', i)

    print(threading.current_thread())


def sum():
    print('sum:', add_num)


if __name__ == '__main__':
    # for i in range(20):
    # 用循环创建线程
    sub_thread = threading.Thread(target=unord)
    sub_thread.start()

    time.sleep(2.0)
    # 多线程之间共享全局变量，比如这里的
    sub_sum = threading.Thread(target=sum)
    sub_sum.start()
    # 线程之间执行是无序的，具体先执行哪个是由cpu调度决定的,操作系统调度进程
time.sleep(0.2)
# 主线程会等所有的子线程执行完成后才会结束程序
print('over')

