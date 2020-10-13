# 线程执行带有参数的任务
import threading


# 显示任务信息
def show_info(name, age):
    print('name:%s age:%d'%(name,age))


# 创建子线程
# 以元组的方式进行传参,元组里面的参数要和函数里的参数顺序一致
sub_thread = threading.Thread(target=show_info, args=('王五', 20))
# 启动线程
sub_thread.start()

# 以字典的方式进行传参,字典里的key和函数里的参数名保持一致即可
# sub_process = multiprocessing.Process(target=show_info, kwargs={'name':'小赵','age':20})
# # 启动进程
# sub_process.start()

# sub_thread = threading.Thread(target=show_info, args=('李四',),kwargs={'age':20})
# sub_thread.start()