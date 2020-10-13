import multiprocessing
import time

g_list = list()
multiprocessing.Queue()


def add_data():
    for i in range(3):
        g_list.append(i)
        print('add:', i)
        time.sleep(0.1)
    print('添加数据：', g_list)


def read_data():
    print(g_list)


# 在linux和mac中不需要使用这行语句，但是在win中必须写，否则会递归拷贝主进程的数据
# 直接执行的模块就是主模块，那么直接执行的模块里面就应该添加判断是否是主模块的代码
# 1.防止别人导入文件时候执行main里面的代码
# 2.防止win递归创建子进程
if __name__ == '__main__':
    # 创建子进程写入数据
    add_process = multiprocessing.Process(target=add_data)
    # 创建主进程读取数据
    read_process = multiprocessing.Process(target=read_data)

    # 执行子进程
    add_process.start()
    # 当前进程等待add_process执行完成后再执行下面的程序
    add_process.join()
    read_process.start()


# 结论：进程之间不共享全局变量,创建子进程其实就是对主进程资源的拷贝。


print('啥时候执行')

