# property属性就是负责把一个方法当做属性去使用，这样可以简化代码
# 定义property属性有两中国方式：1.装饰器方式  2.类属性方式
# class Student(object):
#     def __init__(self):
#         self.__age = 0
#
#     def age(self):
#         return self.__age
#
# student = Student()
# # 这里是调用方法
# age = student.age()
# print(age)


# class Student(object):
#     def __init__(self):
#         self.__age = 0
#
#     @property
#     def age(self):
#         print("这里调用属性了")
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         print("这里修改值了")
#         if 0 <= new_age <= 130:
#             self.__age = new_age
#
#         else:
#             print("成精了")
#
#
# student = Student()
# # 调用属性
# age = student.age
# print(age)
#
# student.age = 30
# age = student.age
# print(age)

class Person(object):
    def __init__(self):
        self.__age = 0

    def get_age(self):
        # 当获取age属性时候会执行该方法
        return self.__age

    def set_age(self, new_age):
        """当设置age属性时候会执行该方法"""
        if new_age >= 150:
            print("成精了")

        else:
            self.__age = new_age

    # 类属性方式的property属性
    # property的参数说明：第一个参数是获取属性时候要执行的方法，第二个参数是设置属性时要执行的方法
    age = property(get_age, set_age)


p = Person()
print(p.age)
p.age = 100
print(p.age)
p.age = 1000

"""
定义property属性有两种方法：
装饰器方式：
1.@property修饰装饰器的方法
2.@方法名.setter修饰设置值的方法
类属性方式：
1.类属性 = property（获取值方法，设置值方法）
"""
