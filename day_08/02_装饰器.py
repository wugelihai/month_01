"""
装饰器就是给已有的函数增加额外的功能，它本质上就是一个闭包函数
功能特点：
1.不修改已有函数的源代码
2.不修改已有函数的调用方式
3.给已有函数增加额外的功能

说明：
闭包函数有且只有一个参数，必须是函数类型，这样定义的函数才是装饰器
写代码要遵循开放封闭原则，他规定已经实现的功能代码不允许被修改，但可以被扩展
"""
# 这部分是装饰器，用来装饰下面发表评论的函数
# def check(fn):
#     def inner():
#         print("请先登录。。。。")
#         fn()
#     return inner()
#
# @check
# def comment():
#     print("发表评论。。。。")
#
#
# comment()

"""
装饰器的标准格式：
def decorator(fn):   # fn是想要被装饰的函数
    def inner():
        '''执行函数之前'''
        fn()
        '''执行函数之后'''
    return inner
    
@decorator
def fn()


然后在下面正常的调用fn(),就会得到被装饰后的效果
"""


# 装饰器的实际使用
# 用装饰器统计函数执行时间
# import time
#
#
# def get_time(fun):
#     def inner():
#         start_time = time.time()
#         fun()
#         end_time = time.time()
#         print("函数执行共耗时:", end_time - start_time)
#     return inner
#
# @get_time
# def test():
#     print("函数开始执行了")
#     time.sleep(5)
#     print("函数执行结束")
#
# test()


# 装饰带有参数的函数
# 定长
# def loogin(fn):
#     def inner(num1,num2):
#         print("---正在计算---")
#         result = fn(num1,num2)
#         return result
#     return inner
#
#
# @loogin
# def sum_num(a,b):
#     sum = a+b
#     return sum
#
#
# result = sum_num(2,3)
# print(result)

# 通用函数装饰器，也就是不定长的，使用*args和**kwargs


# 多个装饰器：多个装饰器对一个函数进行装饰
# def make_div(func):
#     def inner(*args, **kwargs):
#         return "<div>" + func() + "</div>"
#
#     return inner
#
#
# def make_p(func):
#     def inner(*args, **kwargs):
#         return "<p>" + func() + "</p>"
#     return inner
#
# # 多个装饰器可以想象成包裹的样子，最外层的包裹里面所有的层数
# @make_div
# @make_p
# def content():
#     return "人生苦短"
#
# result = content()
# print(result)


# 带有参数的装饰器
# 这种是错误的写法，因为装饰器只能接受一个参数，而且还必须是函数类型
# def decorator(fn, flag):
#     def inner(num1, num2):
#         if flag == "+":
#             print("正在计算加法。。。。")
#
#         if flag == "-":
#             print("正在计算减法。。。。")
#
#         result = fn(num1, num2)
#         return result
#
#     return inner
#
#
# @decorator("+")
# def add(num1, num2):
#     result = num1 + num2
#     return result
#
#
# result = add(1, 2)
# print(result)


# 正确写法：在装饰器外层在包裹一个函数，让最外面的函数接收参数，返回的是装饰
# def loggin(flag):
#     def decorator(fn):
#         def inner(num1, num2):
#             if flag == "+":
#                 print("正在计算加法。。。。")
#
#             if flag == "-":
#                 print("正在计算减法。。。。")
#
#             result = fn(num1, num2)
#             return result
#
#         return inner
#
#     # 返回装饰器
#     return decorator
#
#
# @loggin("+")
# def add(num1, num2):
#     result = num1 + num2
#     return result
#
#
# @loggin("-")
# def sub(num1, num2):
#     result = num1 - num2
#     return result
#
#
# result1 = add(1, 2)
# result2 = sub(2, 1)
# print(result1, result2)

# 类装饰器：通过定义一个类来装饰函数
# 想要让类的实力对象能够像函数一样进行调用，需要在类里面使用call方法，把类的实例编程可调用对象
# 类的装饰函数功能在call方法里面进行添加
class Check(object):
    def __init__(self, fn):
        # 初始化操作在这里完成
        self.__fn = fn

    # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
    def __call__(self, *args, **kwargs):
        # 添加装饰功能
        print("请先登录。。。。")
        self.__fn()


@Check
def comment():
    print("发表评论")


comment()
