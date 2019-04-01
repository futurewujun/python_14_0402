# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 20:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_函数的参数类型.py

# def count_number(c,a=1,b=101,):#形参
#     count=0
#     for i in range(a,b,c):#range(1,4,2)#1 3
#         count+=i#count=count+i
#     print('计算结果是：{}'.format(count))
#     return count#隐式的添加
#
# # count_number(0,101,2)
# count_number(2,a=0)#实参

#1：函数的参数个数大于等于0个都行
#2:为什么要加参数，还是要提高代码的复用性,参数通过函数的参数列表传递进来

#参数的类型：位置参数  默认参数 动态参数 关键字参数
'''1:位置参数：是有顺序的 我们通过函数传参的时候  是按顺序赋值
#形参 实参
#指定参数赋值  声明赋值  变量名要跟形参一致
#调用函数的时候  有几个位置参数 就要传几个参数'''
# count_number(c=2,a=0,b=101)

'''2：默认参数：我们给形参指定一个默认值
#.有实参就用实参 没实参才用默认参数值
#.位置参数 应该在默认参数之前'''

'''3.动态参数 *args 不定长参数 你想传几个 就传几个 参数之间用逗号隔开
#1:可以传任意多个参数，不限制数据类型，参数之间用逗号隔开
#2：参数到了函数内部 就变成了元组
#3：args 默认写这个  一定要有星号 * '''
# def robot_cat(*args):
#     print(args)
#     for item in args:
#         print('我是叮当猫，我可以变出好多好多好多东西，比如有：{0}'.format(item))
# #
# robot_cat('20k的offer','钱钱钱','女朋友','龙虾','任意门','豪宅','时空机',
#           '后悔药',2000000)

# a=[['20k的offer','钱钱钱'],['女朋友','龙虾']]
# b={'name':'小桃子','offer':'18k'}
# robot_cat(b)
#脱外套 只脱一层

'''4.关键字参数 **kwargs key value的形式 key word arguments
#1:key value的形式参数之间用逗号隔开
#2：参数到了函数内部 就变成了字典  '''

# def anyway(**kwargs):
#     print(kwargs)
# anyway(x=1,b=2,c=4,name='huahua')#英文字母