# print('hello world')
#
# message = 'hello world'
# print(message)

# name1 = 'jetty'
# name2 = 'zhao'
# print(name.title())
# print(name.upper())
# print(name.lower())
# name = name1 + name2
# print(name)

# language = 'python\nJavascript\nc\nrust'
# # print(language)

# black = ' python '
# print(black.rstrip())
#
#
# num = 2.330
# print(int(num))
# print(float(num))

# color = ['red','green','yellow','pink']
# print(color[0])
# color[0] = 'black'
# print(color[0])
# color.append('orange')
# print(color)

# color.insert(0,'blue')
# print(color)
#
# del color[0]
# color.pop()
# color.remove('yellow')
# print(color)

# num_list = [11,2,3,42,1,5,6]
# num_list.sort()
# print(num_list)

# 临时排序
# print(sorted(num_list))
# print(num_list)
#
# num_list.reverse()
# print(num_list)

# print(len(num_list))

# for i in range(len(num_list)):
#     print(num_list[i],end = '\n')

#乘方运算
# squares = []
# for i in range(1,6):
#     squares.append(i**2)
# print(squares)

# 内置函数 min max sum
# print(sum(num_list))
# print(min(num_list))

# 1-50基数和
# num = 0
# for i in range(1,51,2):
#     num = num + i
# print(num)

# 3-90,3的倍数的和
# num = 0
# for i in range(3,100):
#     if i%3 == 0:
#         num = num+i
# print(num)

# list1 = []
# for i in range(1,10):
#     list1.append(i**3)
# print(list1)

# squares = [i**3 for i in range(3,10)]
# print(squares)

# 列表切片
# num_list = [1,2,3,4,2,1,3,1,2]
# print(num_list[0:5])

# 元组，不可改变
# for i in num_list:
#     if i % 2== 0:
#         print(i)

# for i in num_list:
#     if i %2 != 0:
#         print(i)


# 字典
# aliyun = {'color':0,'points':1}
# print(aliyun['color'])
# aliyun['color'] = 'red'
# print(aliyun)

# ipt = input('你是小黄么')
# if ipt == '1':
#     print('是本人')
# else:
#     print('不是本人')

# count = 0
# arr = []
# while count < 20:
#     for j in range(1, 100):
#         if j % 11 == 0:
#             count = count+1
#             arr.append(j)
# print(arr)

# def num_sum(arr):
#     result = 0
#     for i in arr:
#         result = result+i
#     return result
#
#
# print(num_sum([1,2,3]))

# def make_prize(*top):
#     return top
#
#
# print(make_prize(1))
# print(make_prize(1,2,3))
# print(make_prize(1,3,4,5))
# print(make_prize(1,1,1,1,1))


# username = input('请输入用户口令：')
# passwd = input('请输入口令：')
# # 默认用户名为admin，密码为123456，相同则成功登陆，不相同则验证失败
# if username == 'admin' and passwd == '123456':
#   print('登录成功')
# elif username != 'admin':
#   print('用户名错误！')
# elif username == 'admin' and passwd != '123456':
#   print('密码错误！')


# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print(f'f({x}) = {y}')

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

# 前两个数都是1
# a, b = 1, 1
# print(a, b, end=' ')
# # 通过递推公式算出后面的18个数
# for _ in range(18):
#     a, b = b, a + b
#     print(b, end=' ')

# from random import randint
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     """三个数相加"""
#     return a + b + c

#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))


# def foo():
#     print('hello, world!')
#
#
# def foo():
#     print('goodbye, world!')
#
# foo()

# import random
# import string
#
#
# verify_code = string.ascii_letters + string.digits
#
# def code(code_len = 4):
#     s = ''.join(random.choices(verify_code , k = code_len))
#     return s
#
# print(code(6))

# from os.path import splitext
# #
# #
# # def get_suffix(filename):
# #     return splitext(filename)[1][1:]
# #
# # print(get_suffix('readme.txt'))

import os
import time

# content = '北 京 欢 迎 你 为 你 开 天 辟 地           '
# while True:
#     # Windows清除屏幕上的输出
#     # os.system('cls')
#     # macOS清除屏幕上的输出
#     os.system('clear')
#     print(content)
#     # 休眠0.2秒（200毫秒）
#     time.sleep(0.2)
#     content = content[1:] + content[0]


# import random
#
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randint(1, 6)
#     counters[face - 1] += 1
# for face in range(1, 7):
#     print(f'{face}点出现了{counters[face - 1]}次')


# scores = [[0] * 3 for _ in range(5)]
# print(scores)
# scores[0][0] = 3
# print(scores)

# persons = [True] * 30
# # counter - 扔到海里的人数
# # index - 访问列表的索引
# # number - 报数的数字
# counter, index, number = 0, 0, 0
# while counter < 15:
#     if persons[index]:
#         number += 1
#         if number == 9:
#             persons[index] = False
#             counter += 1
#             number = 0
#     index += 1
#     index %= 30
# for person in persons:
#     print('女' if person else '男', end='')


# set1 = frozenset({1,2,3})
# set2 = frozenset(range(10))
# print(set1,set2)


# import random
# import time
#
#
# def download(filename):
#     print(f'开始下载{filename}.')
#     time.sleep(random.randint(2, 6))
#     print(f'{filename}下载完成.')
#
#
# def upload(filename):
#     print(f'开始上传{filename}.')
#     time.sleep(random.randint(4, 8))
#     print(f'{filename}上传完成.')
#
#
# # 定义装饰器函数，它的参数是被装饰的函数或类
# def record_time(func):
#
#     # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
#     # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
#     # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
#     def wrapper(*args, **kwargs):
#         # 在执行被装饰的函数之前记录开始时间
#         start = time.time()
#         # 执行被装饰的函数并获取返回值
#         result = func(*args, **kwargs)
#         # 在执行被装饰的函数之后记录结束时间
#         end = time.time()
#         # 计算和显示被装饰函数的执行时间
#         print(f'{func.__name__}执行时间: {end - start:.3f}秒')
#         # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
#         return result
#
#     # 返回带装饰功能的wrapper函数
#     return wrapper
#
#
# @record_time
# def add(a):
#     time.sleep(3)
#     print(a**100)
#
#
# download = record_time(download)
# upload = record_time(upload)
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')
#
#
# add(16)

a = 1
b = 1
c = 0
while c < 10:

    print(a)

    a, b = b, a+b
    c += 1










