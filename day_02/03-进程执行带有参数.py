# 进程执行带有参数的任务
import multiprocessing


# 显示任务信息
def show_info(name, age):
    print(name, age)


# # 创建子进程
# # 以元组的方式进行传参,元组里面的参数要和函数里的参数顺序一致
# sub_process = multiprocessing.Process(target=show_info, args=('王五', 20))
# # 启动进程
# sub_process.start()

# 以字典的方式进行传参,字典里的key和函数里的参数名保持一致即可
# sub_process = multiprocessing.Process(target=show_info, kwargs={'name':'小赵','age':20})
# # 启动进程
# sub_process.start()

sub_process = multiprocessing.Process(target=show_info, args=('你好',),kwargs={'age':20})
sub_process.start()