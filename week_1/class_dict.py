# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 21:34
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_dict.py

#字典 关键字  dict  dictionary  符号 {}
##1:特征
#>1.1.大括号括起来的数据，都是字典，看类型 type
#>1.2.空字典 d={}
#>1.3.字典里面元素存储的方式 key：value的形式  键值对
#key  不可变，唯一  int  str tuple float
#value 数据类型不限 整数 浮点数 字符串 布尔值 True--1 False--0 元组 列表 字典
#key:value键值对 用逗号区分开来的

#>1.4.取值方式：无序的数据
#根据key取值 字典名[key]
a={}
d={"name":'执着',
   'hobby':'学Python',
   'age':18,
   'score':{'en':120,'math':99.99,'ch':'A'},
   'friend':['bay max','小CC','如意'],
   'good_man':True,
   0.02:'python',
   False:'这个value对应的key是布尔值',
  (1,2,3):'我就是元组大大！！！'}
for q in d:
   print(q)
# print(d['friend'][0])
# #字典嵌套取值
# print(d['score']['en'])
for i in d:
   print(d[i])
   a[i]=d[i]
print(a)
print(d)



#>1.5.支持增删改
#增加  d[key] key是不存在字典里面  就是新增
d['salary']='20k'
# print(d)
#修改 d[key] key是存在字典里面  就是修改
# d['name']='幽幽'
# print(d)

#删除：根据key去删除
d.pop('friend')
# print(d)

#随机删除--了解即可
# d.popitem()
# print(d)

# print(d.keys())#获取字典的所有key
# print(d.values())#获取字典的所有value

#下次上课的重点：
#if 。。else  循环语句 for while
#难点