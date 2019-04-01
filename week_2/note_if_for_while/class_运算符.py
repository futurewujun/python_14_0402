# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 20:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_运算符.py

#1:算术运算符  + - * /  % 取余运算 6%5
# print(6%5)
#取数运算干啥？？？ 判断一个数是否是奇数还是偶数
#我们在哪里还用过 +  字符串的拼接 列表的合并

#2:赋值运算符 = += -=
# a=3
# a-=4#a=a-4
# print(a)

#3:比较运算符 == > >= < <= !=
#运算结果： 布尔值  True False
# print(3==4)
# print(3!=4)
# print(3>4)
# print(3<4)

# print('get'.upper()=='GET')#字母是区分大小写

#4:逻辑运算符 and or not(自己去拓展）not>and>or
#运算结果： 布尔值  True False
# a=10
# b=-5
# c=0
# # print(a>0 and b>0)#且,与   左右两边同时满足才为真
# # print(a>0 or b>0)# 或     左右两边只要有一边满足即可
# # print(a>0 and b>0 and c>0)
# # print(a>0 or b>0 and c==0)

#5:成员运算符 in 、not in
#运算结果： 布尔值  True False
# str_1='hello'
# print('0' in str_1)

# t=[1,'hello',666,9.09]
# print('h' in t)

d={'name':'小cc','age':22}#根据key去判断
print('age' not in d)