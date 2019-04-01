# -*- coding: utf-8 -*-
# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
# def judge_exist(dt):
#     print("字典传入成功！", dt)
#     value = [i for i in dt.values()]
#     sr = input("请输入字符串：")
#     choice = input("是否将数字转换为整数（y or n）：")
#     str_result =int(sr) if choice == 'y' else sr
#     print(str_result,type(str_result))
#     if str_result in value:
#         print("该字符串在字典中！")
#     else:
#         print("字符串不在字典中！")
#         dt["new_key"] = str_result
#         print("已将该字符串添加进字典：", dt)
# while 1:
#     try:
#         input_dict = input("请传入一个字典:")
#         dt = eval(input_dict)
#         print(dt,type(dt))
#     except:
#         print("\t请输入字典格式！")
#     else:
#         if type(dt).__name__=='dict':
#             judge_exist(dt)
#             break
#         else:
#             print("\t请输入字典格式！")


# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
# sum = 0
# def get_people(gender, age):
#     global sum
#     if gender == 'f' and 10 <= int(age) <= 15:
#         sum += 1
#         print("你的条件满足加入足球队，已记录")
#     else:
#         print('你的条件不满足加入足球队！')
# count = 0
# # sum = 0
# while count < 3:
#     gender = input("请输入你的性别（m 表示男性，f表示女性）：")
#     age = input("请输入你的年龄：")
#     get_people(gender, age)
#     count += 1
#     if count == 3:
#         print("满足条件的总人数为：%d" % sum)


# 2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。 比如这个字符串： 我的名字是lemon,今年5岁。 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。

import string
print(string.digits)  # 输出包含数字0~9的字符串
print(string.ascii_letters)#输出大小写字母
print(string.punctuation)#输出特殊字符
a=input("请输入一段话：")
num=[]
en=[]
cn=[]
si=[]
for i in a:
    if i in string.digits:#数字
        num.append(i)
    elif i in string.ascii_letters:#字母
        en.append(i)
    elif (i in string.punctuation) or (i in "，。？！："):#符号
        si.append(i)
    else:
        cn.append(i)
print("数字：",' '.join(num))
print("字母：",' '.join(en))   # 将空格加到en中
print("汉字：",' '.join(cn))
print("符号：",' '.join(si))
