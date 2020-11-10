# 根据程序制定规则循环生成数据，当条件不成立时，则生成数据约束，数据不是一次性全部横撑处理，而是使用一个生成一个，可以节约大量内存
# 创建生成器方式：生成器推导式，yield关键字
# 生成器推导式：(和列表推导时很像)
# my_generator = (i * 2 for i in range(5))
# print(my_generator)

# vaule = next(my_generator)
# print(vaule)

# # 遍历生成器
# for vaule in my_generator:
#     print(vaule)


# yield关键字
# 只要在def函数里面看到有yield关键字那么就是生成器
# def mygenerater(n):
#     for i in range(n):
#         print('开始生成。。。。')
#         yield i
#         print('完成一次')
#
# if __name__ == '__main__':
#     g = mygenerater(2)
#
#     for i in g:
#         print(i)

# 斐波那契数列生成式
def fibonacci(num):
    a = 0
    b = 1
    current_index = 0

    while current_index < num:
        result = a
        a, b = b, a + b
        current_index += 1
        yield result


fib = fibonacci(100)
for i in fib:
    print(i)

"""
代码执行到yield会暂停，然后把结果返回出去，下次启动生成器会在暂停的位置继续往下执行
生成器如果把数据生成完成，再次获取生成其中的一个数据会泡出一个Stoplteration异常，表示停止迭代异常
while循环内部没有异常处理操作，需要手动添加处理异常时间的操作
for循环内部自动处理了迭代异常，使用起来更加方便
"""
