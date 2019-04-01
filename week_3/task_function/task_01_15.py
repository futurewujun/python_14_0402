# -*- coding: utf-8 -*-
# Created by xj on 2019/1/15

"""进阶提升题：
1：利用字符串所学内置函数，完成如下题目，具体使用的函数已经提示过了~在课堂上，请去视频里面找答案！
请用自己目前所学实现指定字符串大写转小写，小写变大写，并且将字符串变为镜像字符串，
镜像的意思是：大写的’A’变为’Z’,’大写的‘B‘变成‘Y,小写的’’’b’变为’y 。目前要求处理的示范
字符串是： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa” 需要提供至少2种不同的解决方法。"""
#===解法1========================================================================
# str_1 ="sdSdsfdAdsdsdfsfdsdASDSDFDSFa" #声明字符串存储变量
# str_2 =str_1.swapcase()  #str_1调用内置函数swapcase大小写互换
# print(str_2) #打印str_2到控制台
# str_3 = str.maketrans("ABb","ZYy") #利用字符串内置函数makestrans将所需替换的ABb替换称目标字符串ZYy
# print(str_3)
# str_4 = str_2.translate(str_3) #根据str3的映射规则 将str_2中字符进行替换，生成新字符串
# print(str_4)
#====解法2=======================================================================
# str_1 ="sdSdsfdAdsdsdfsfdsdASDSDFDSFa"#声明字符串存储变量
# str_4 =""#创建空的字符串
# for item in str_1:  #遍历str_1中的字符
#     if item.islower():#判断字符是否为小写
#         str_2 = item.upper() #将小写字母变为大写，将返回值赋予str_2
#         str_4+=str_2  #字符串拼接
#     else:
#         str_3 =item.lower() #将大写字母变为小写，将返回值赋予str_3
#         str_4 +=str_3  #字符串拼接
# print(str_4) #打印新生成大小写互换字符串
# str_5 = str_4.replace("A","Z").replace("B","Y").replace("b","y") #进行替换并将返回值付给str_5
# print(str_5)
"""
搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。 
比如这个字符串： 我的是名字是lemon,今年5岁。  语法分析后得到结果如下： 
数字：5 
中文：我的名字是、今年、岁 
拼音：lemon
符号：，。 请编写程序实现该词法分析功能。 """
import re
#===========数字=========================
def isnumber():
    str_1 = "我的是名2字是lemon,今年5岁。"
    k1 = re.compile(r'\d+')  #正则编译模式
    list_1 =re.findall(k1,str_1) #查找字符串中匹配项
    s1 = "数字：" #建立一个字段字符串
    for num in list_1: #从正则列表中匹配到的数字进行遍历
        t1 = s1+ num +" " #将遍历得到的字符拼接
        s1 = t1          #将拼接后的字符串赋值给变量s1  让s1在去拼接
    print("{}".format(s1))  #输出字符串以数字：num1 num2 num3 形式

#========符号===========================
def symbol():
    str_1 = "我的是名字op是lemon,今年5岁。"
    k4 = re.compile("[,。]+")  #匹配字符串中的，及。
    list_4 =re.findall(k4,str_1) #遍历列表中，及。
    s4="符号："#建立一个初始字符串
    for t in list_4:  #遍历字符串拼接
        str_4 = s4 + t + " "
        s4 = str_4
    print(s4)
#===========中文=============================
def china():
    str_1 = "我的是名字是lemon,今年5岁。"
    k5 = re.compile(r"[,。]") #匹配字符串中的，及。
    list_5 = k5.findall(str_1) #遍历列表中，及。
    s5 ="中文："
    for i in list_5: #遍历将字符串中，及。替换称空字符串
        str_6 = str_1.replace(i,"")
        str_1 = str_6
    k2 = re.compile(r'[u4e00-u9fa5]+') #匹配空字符串中字母，数字
    list_2 = k2.findall(str_1)
    for num_2 in list_2: #遍历列表中字母，数字
        str_3=str_1.replace(num_2,"、") #将列表中匹配到的字母及数字替换称顿号
        str_1=str_3
    print(s5 +str_1)  #拼接输出
#===========拼音==================
def char():
    str_1 = "我的是名ll字是lemon,今年5岁。"
    k6 =re.compile(r"[a-zA-Z]+") #匹配字符串中大小写字母
    list_6 = k6.findall(str_1)
    s6="拼音:"
    for i in list_6: #遍历出列表中的大小写字母
        str_6 = s6 + i + " "#遍历拼接
        s6 = str_6
    print(s6)
isnumber() #函数调用
china()
char()
symbol()



# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# from collections import Iterable
# def count_length(x):
#     if isinstance(x,Iterable):
#         s = len(x)
#         if s > 5:
#             print("所传入{}长度大于5".format(x))
#         else:
#             print("所传入的{}的长度小于5".format(x))
#     else:
#         print("你输入的{}不符合需求".format(x))
# list_1 = [1,2,3,4,3,4,5]
# str_1 ="adnnn"
# data_1={"name":"1","age":"12"}
# count_length(str_1)
# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# def func(data_1):
#     if len(data_1) > 2:
#         data_2 = data_1[0:2]
#     else:
#         print("你输入的列表长度小于2")
#     return data_2
# data_1 = [1,2,3,4,5,6]
# print(func(data_1))
# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
# def add_key(data,str_1):
#
#     if str_1 not in data.values():
#         data[str_1]=str_1
#     else:
#         print("该字符串中在字典中已经存在")
#     return data
# data ={"name":"tom","age":"23"}
# str1 ="python"
# print(add_key(data,str1))

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数
#
# def isnumber(num):
#     num = True
#     try:
#         num = int(num)
#     except ValueError:
#         return False
#     return True
# def add_memeber(x,y):
#     total = 0
#     satifitied_person = 0
#     while total<10:
#         age = input("请问你几岁了?")
#         input_age = age.strip()
#         if isnumber(input_age):
#             input_age = int(input_age)
#             if x <=input_age<=y:
#                 sex_input = input("请问你的性别是m or f?")
#                 if sex_input == "m":
#                     print("很遗憾，你不能加入")
#                 else:
#                     print("恭喜你加入")
#                     satifitied_person +=1
#             else:
#                 print("你的年龄不符合要求")
#         else:
#             print("你输入的年龄有误")
#         total +=1
#     return satifitied_person
# sum_num =add_memeber(10,12) #符合条件的人数
# print(sum_num)
