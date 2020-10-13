# 进程负责要内存，线程负责要cpu
# 默认一个进程里面有一个线程，一个进程里面可以有多个线程
# 单进程多线程之间是可以共享全局变量的

# 按住command打开的是 名字.py文件，那么就是模块，如果打开的是__init__.py那么就是包


# 1.导入线程模块    2.创建子线程    3.启动子线程执行对应的任务
import threading
import time


# 创建唱歌线程
def sing():
    # 获取线程编号
    sing_current = threading.current_thread()
    print('sing_current:', sing_current)
    for i in range(3):
        print('唱歌中。。。')
        time.sleep(0.3)


# 创建跳舞线程
def dance():
    # 获取线程编号
    dance_current = threading.current_thread()
    print('dance_current:', dance_current)
    for i in range(3):
        print('跳舞中。。。')
        time.sleep(0.2)


# 这个一定要写
if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing,name='sing')

    dance_thread = threading.Thread(target=dance,name='dance')

    sing_thread.start()
    dance_thread.start()

