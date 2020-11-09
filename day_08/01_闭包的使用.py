# 测试闭包函数的使用
# 闭包函数可以提高代码的重用性，不需要定义额外的功能函数
# def config_name(name):
#     def say_info(info):
#         print(name + ":" + info)
#
#     return say_info
#
# tom = config_name("Tom")
# jack = config_name("Jack")
#
# tom("你好，在么")
# jack("不在")
# tom("出来玩嘛")
# jack("不去")


"""
闭包函数的标准格式：
1.函数的嵌套
2.函数嵌套前提下内部函数调用了外部函数的变量或者参数
3.外部函数返回来内部函数（不带括号的那种）

def test1(a):
    def test2(b):
        print(a+b)
    return test2

num = test1(1)
num(2)
num(3)
"""

# 修改闭包函数使用的外部变量：使用nonlocal
# def test1(a):
#     def test2(b):
#         nonlocal a
#         a = 100
#         print(a+b)
#     return test2
#
# num = test1(1)
# num(2)
# num(3)
