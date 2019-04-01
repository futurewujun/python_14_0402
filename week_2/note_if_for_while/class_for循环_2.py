# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 9:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_for循环_2.py

#for循环的作用：1：遍历元素  2：可以控制循环次数
#for循环可用来遍历的数据类型：str tuple list dict ---目前所学的
#还有很多数据类型  只要是可迭代的 就可以用for循环来遍历
#可迭代的数据类型：数据里面允许存在多个元素的
#如果用整数 int类型：TypeError: 'int' object is not iterable  不可迭代

#想办法：怎么利用函数去判断我的数据类型是可迭代的--自己去找

# d={'name':'katt','age':18,'money':'10w'}
# a=0
# for item in d.values():
#     a+=1
#     print('这是第{}次循环'.format(a))
#     print(item)
#     print()#换行

#range函数：生成一个整数序列  可迭代的对象
#range(m,n,k)# m开头的数字 n结尾的数字 k步长,默认值为1 取左不取右
#如果range(m,n) k默认为1
#如果range(n) m默认为 0
# res=range(1,10,5)
# print(set(res))#强转列表 为了方便你们观察我们拿到的到底是什么？

# res=range(1,10)#
# print(set(res))
#
# res=range(10)
# print(list(res))


#题目 我要生成0-100的数字
# res=range(0,101)
# print(list(res))

# 1：写一段程序，分别求出0-100之间的所有数之和。
# sum=0#初始值 用来存储我们求的和
# for item in range(101):
#     sum=sum+item
# print(sum)

# 1：写一段程序，分别求出0-100之间的所有偶数的和和所有奇数的和。
#解法1：
# sum_1=0#初始值 用来存储我们奇数和
# for item in range(1,101,2):#1 3 5
#     sum_1=sum_1+item
# print('奇数和:',sum_1)
#
# sum_2=0#初始值 用来存储我们偶数和
# for item in range(0,101,2):#0 2 4 6
#     sum_2=sum_2+item
# print('偶数和:',sum_2)

#解法2：
# sum_1=0#初始值 用来存储我们奇数和
# sum_2=0#初始值 用来存储我们偶数和
# for item in range(101):
#     if item%2==0:#说明这个数是偶数
#         sum_2=sum_2+item
#     else:#否则就是奇数
#         sum_1=sum_1+item
# print('奇数和:',sum_1)
# print('偶数和:',sum_2)

#嵌套循环：循环里面还有循环
# P=[[1,2,3],[4,5,6],[7,8,9]]
# for a in P:#外层循环
#     for item in a:#内层循环
#         print(item)
# *
# **
# ***
# ****
# *****
# P=[['*'],['*','*'],['*','*','*'],['*','*','*','*'],['*','*','*','*','*']]
# for i in range(1,6):#1 2 3 4 5 i=1 i=2
#     for j in range(1,i+1):#range(1,2) range(1,3)
#         print('*',end='')
#     print()

# for i in range(1,6):#1 2 3 4 5 i=1 i=2
#     print(i*'*',end='')
#     print()
