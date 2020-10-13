# 1.导入进程包
import multiprocessing
import time
import os


# 跳舞任务
def dance():
    dance_process_id = os.getpid()
    print('dance_process_id:', dance_process_id, multiprocessing.current_process())
    # 获取这个子进程的父进程编号
    dance_process_parents_id = os.getppid()
    print('sing_process_parents_id的主进程编号是:', dance_process_parents_id)
    for i in range(3):
        print('跳舞中。。。')
        time.sleep(0.3)
        # 知道进程编号之后，可以强制杀死进程， -9代表强制杀死
        os.kill(dance_process_id, 9)


# 唱歌任务
def sing():
    sing_process_id = os.getpid()
    # 获取当前进程对象，查看当前进程是由哪个代码执行的:multiprocessing.current_process()
    print('sing_process_id:', sing_process_id, multiprocessing.current_process())
    # 获取这个子进程的父进程编号
    sing_process_parents_id = os.getppid()
    print('sing_process_parents_id的主进程编号是:', sing_process_parents_id)
    for i in range(3):
        print('唱歌中。。。')
        time.sleep(0.3)


# 获取当前进程编号
main_process_id = os.getpid()
# 获取当前进程对象，查看当前进程是由哪个代码执行的:multiprocessing.current_process()
print('main_process_id:', main_process_id, multiprocessing.current_process())

# 2.创建子进程（自己手动创建的进程为子进程）
# 参数：group：进程组，目前只能使用None，一般不需要设置   target：进程执行的目标任务    name：进程名，如果不设置，默认是Process -1
dance_process = multiprocessing.Process(target=dance)
print('dance_process:', dance_process)
sing_process = multiprocessing.Process(target=sing)
print('sing_process:', sing_process)

# 3.启动进程执行对应的任务
dance_process.start()
sing_process.start()

# 进程是无序的，具体限执行哪个，是由操作系统调度决定的
