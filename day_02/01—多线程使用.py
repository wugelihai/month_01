# 1.导入进程包
import multiprocessing
import time


# 跳舞任务
def dance():
    for i in range(3):
        print('跳舞中。。。')
        time.sleep(0.3)


# 唱歌任务
def sing():
    for i in range(3):
        print('唱歌中。。。')
        time.sleep(0.3)


# 2.创建子进程（自己手动创建的进程为子进程）
# 参数：group：进程组，目前只能使用None，一般不需要设置   target：进程执行的目标任务    name：进程名，如果不设置，默认是Process
dance_process = multiprocessing.Process(target=dance)
sine_process = multiprocessing.Process(target=sing)

# 3.启动进程执行对应的任务
dance_process.start()
sine_process.start()


# 进程是无序的，具体限执行哪个，是由操作系统调度决定的


