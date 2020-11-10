import re

"""
匹配单个字符
"""
# 使用match方法进行操作,匹配不到就会报错
# result = re.match("it", "itcast.cn")
# info = result.group()
# print(info)

# .  匹配任意一个字符，除了\n
# ret = re.match(".", "M")
# print(ret.group())
# ret = re.match("w.o", "weo")
# print(ret.group())

# []匹配中括号中列举的字符
# ret = re.match("[hH]ello", "hello world")
# print(ret.group())
# 这里表示两段序列，从0-4到6-9，如果选择5是匹配不到的
# ret = re.match("[0-46-9]", "7我的世界")
# print(ret.group())


# \d 匹配数字
# ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
# print(ret.group())

# \D匹配非数字
# match_obj = re.match("\D","fwoda")
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

# \s 匹配空白字符，即空格，tab键,回车键
# ret = re.match("hello\sworld","hello\nworld")
# print(ret.group())

# \S匹配非空白
# ret = re.match("hello\Sworld","hello$world")
# print(ret.group())

# \w匹配非特殊字符，下划线属于非特殊字符_
# ret = re.match("hello\wworld","hello_world")
# print(ret.group())


# \W匹配特殊字符

# ret = re.match("hello\Wworld","hello^world")
# print(ret.group())

"""
匹配多个字符
"""
# * 匹配*号的前一个字符出现0次或者无限次，即可有可无
# ret = re.match("[A-Z][a-z]*","MBBB")
# print(ret.group())
#
# ret = re.match("[A-Z][a-z]*","Mabcdefg")
# print(ret.group())
#
# ret = re.match("[A-Z][a-z]*","MabcdefG")
# print(ret.group())

# +匹配加号的前一个字符出现1次或者无限次，即至少有1次
# match_obj = re.match("t.+o", "two")
# print(match_obj.group())

# ？匹配前一个字符出现1次或者0次，要么1次，要么没有
# match_obj = re.match("https?", "http")
# print(match_obj.group())

# {m} 匹配前一个字符出现m次
# ret = re.match("[a-zA-Z0-9]{6}","wodshijieshishenme")
# print(ret.group())

# {m,n}匹配前一个字符出现从m到n次
# ret = re.match("[a-zA-Z0-9]{6,11}","wodeshijie")
# print(ret.group())


# 匹配字符串的开头和结尾
# 检查是否以什么开头：用^...这种写法
# ret = re.match("^[hH]", "hello world")
# print(ret.group())

# 检查字符串是否以数字开头,并打印出整个字符串
# match_obj = re.match("^\d.*","1hello")
# print(match_obj.group())

# 检查字符串是否以什么结尾，$
# match_obj = re.match(".*\d$","1hello234")
# print(match_obj.group())

# 匹配以数字开头，中间内容不影响，数字结尾
# match_obj = re.match("^\d.*\d$","1hello234")
# print(match_obj.group())

# 除了指定字符都匹配[^指定字符]
# match_obj = re.match("[^aeiou].*","wodeshijie")
# print(match_obj.group())


# 匹配163邮箱
# match_obj = re.match("^.*@163.com$", "13955448220@163.com")
# print(match_obj.group())


# 匹配11位手机号
# match_obj = re.match("[0-9]{1,11}", "13955448220")
# print(match_obj.group())

# 匹配微博话题
# match_obj = re.match("^#.*#$", "#特朗普#")
# print(match_obj.group())


# 匹配分组
# |   匹配左右任意一个表达式
# fruit_list = ["apple", "banana", "orange", "pear"]
# for i in fruit_list:
#     match_obj = re.match("apple|pear", i)
#     if match_obj:
#         print("%s这个是我需要的" % match_obj.group())
#
#     else:
#         print("%s这个不是我需要的" % i)


# （ab） 将括号中的字符作为一个分组
# 匹配出163,126,qq邮箱等
# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com","1395544@qq.com")
# if match_obj:
#     print(match_obj.group())
#     # 获取分组数据,默认是一个分组，多个分组从左到右依次增加
#     print(match_obj.group(1))
# else:
#     print("匹配失败")

# 匹配qq：1233444这样的数据，提取出qq和qq号码
# match_obj = re.match("(qq):([0-9]\d{4,11})","qq:2223224182")
# print(match_obj.group())
# 分组，默认1是第一个分组，分组从左到右依次增加，（）是分组的单位
# print(match_obj.group(1))
# print(match_obj.group(2))


# \num  引用分组num匹配到字符串
# match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>hh</div>")
# print(match_obj.group())
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")
# 就是匹配第n个分组，与上面的（）分组相结合的

match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>", "<html><h1>hh</h1></html>")
print(match_obj.group())

# (?P<name>)分别起组名
# (？P=name)引用别名为name分组匹配到的字符串
