# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 21:34
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_for循环.py

# s='python13'#8
# L=[1,0.2,'桃子','旅行者','莉红']#5
# t=(1,5,6,'hi','how are you')#5
# d={'name':'katt','age':18,'money':'10w'}#3
# #练习题：
# #请利用for循环 依次打印字典d里面的value值
# for a in d.values():
#     print(a)

#for循环什么关系呢
#什么是循环：单曲循环？
#for循环

# a=0
# for lemon in d:#遍历  利用for循环 依次访问s里面的每一个元素 赋值给item这个变量
#     a+=1#赋值运算
#     print('{0}我要唱 青藏高原！！！'.format(a))
#     print('---------------')

#1：是不是可以访问指定的数据里面的元素？
#2: 还可以利用遍历 去控制循环次数---循环的次数 由什么决定？？ 元素的长度

P=[[1,2,3],[4,5,6],[7,8,9]]
#请一次方位P里面的子列表里面的每个元素 并且打印出来
for a in P:#[1,2,3]
    for b in a:#[1,2,3]
        print(b)


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#for循环  while循环