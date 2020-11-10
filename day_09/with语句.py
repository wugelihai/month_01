# 简化读取文件的操作，使用with语句，既简单又安全，即使有异常，也会关闭文件
# with open("1.txt", "w") as f:
#     f.write("hello world")


# # 自定义上下文管理器
# class File(object):
#     def __init__(self, file_name, file_model):
#         # 定义变量保存文件名和打开模式
#         self.file_name = file_name
#         self.file_model = file_model
#
#     def __enter__(self):
#         print("进入上文方法")
#         # 返回文件资源
#         self.file = open(self.file_name, self.file_model)
#         return self.file
#     # 当with语句执行完成以后，自动执行__exit__方法
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # 负责释放对象资源，比如关闭文件，关闭数据库对象
#         print("进入下文的方法")
#         self.file.close()
#
#
# if __name__ == '__main__':
#     with File("1.txt", "r") as file:
#         file_data = file.read()
#         print(file_data)
# __enter__表示上文方法，需要返回一个操作文件对象
# __exit__表示下文方法，with语句执行完成后会自动执行，即使出现异常也会执行该方法


# 装饰器实现上下文管理器

from contextlib import contextmanager


@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        yield file

    except Exception as e:
        print(e)
    finally:
        print("over")
        file.close()


with my_open('out.txt', 'w') as f:
    f.write("hello world ,my name is Li")
