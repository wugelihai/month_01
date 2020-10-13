# import time
# import tkinter
# import tkinter.messagebox
#
#
# def download():
#     # 模拟下载任务需要花费10秒钟时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成!')
#
#
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者: 赵玉伟(v1.0)')
#
#
# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()

# 多线程去执行任务，把耗费时间的任务设置为一个线程
# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread
#
#
# def main():
#
#     class DownloadTaskHandler(Thread):
#
#         def run(self):
#             time.sleep(10)
#             tkinter.messagebox.showinfo('提示', '下载完成!')
#             # 启用下载按钮
#             button1.config(state=tkinter.NORMAL)
#
#     def download():
#         # 禁用下载按钮
#         button1.config(state=tkinter.DISABLED)
#         # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
#         # 在线程中处理耗时间的下载任务
#         DownloadTaskHandler(daemon=True).start()
#
#     def show_about():
#         tkinter.messagebox.showinfo('关于', '作者: 赵玉伟(v1.0)')
#
#     top = tkinter.Tk()
#     top.title('多线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', 1)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()


# 多进程使用场景，密集型运算
# 不使用多进程进行计算
# from time import time
#
#
# def main():
#     total = 0
#     number_list = [x for x in range(1, 100000001)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print('Execution time: %.3fs' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


# 使用多进程进行计算
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()

