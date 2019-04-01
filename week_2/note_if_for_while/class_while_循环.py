# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 9:36
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_while_循环.py

#for循环：有限次数的循环
#while循环：可以无限次数循环--死循环
#同时 如果加以好好利用 用条件  有条件控制的循环

#while循环语法
#while 条件表达式:
   #循环体

#条件表达式：跟if是一样的
# 1：一般逻辑运算 比较运算 成员运算
# 2: 非0 和非空的数据表示True  为0和为空的数据 表示False（非常重要)
#3:可以直接用布尔值来代替表达式

#运行模式：先判断while后面的条件 满足 就执行循环体  不满足的话 不执行
#执行完毕之后 再次判断while后面的条件  满足 就执行循环体  不满足的话 不执行
#如此反复

#怎么达到 不对绝对的True  也不是绝对的False
#1:基本解决方法：break 终止循环  如果用的不好的话  就是执行一次
#2:进阶使用：break+条件  条件就是你规定他循环多少次
#3:高级使用：必要的时候 脱离break 自由自在
#continue 继续下一次循环
ts = []
for i in range(10):
  if i % 2 == 0:
     continue     # 跳出本次循环，继续执行下一次循环
  ts.append(i)    # 将满足条件的添加进来
print(ts)

# a=0
# while True:
#     a+=1
#     print('a的值',a)
#     print('我是一个死循环{0}'.format(a))
#     if a==10:
#         break
# break是停车 continue就是轻点刹车 刹一下但是还要继续开

#高级使用
# a=0
# while a<10:#a=9
#     a+=1#a=10
#     print('a的值',a)
#     print('我是一个死循环{0}'.format(a))


# 2：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#if 判断
#for循环
#input
#参考if  处理非数字的数据类型

# count=0#记录满足条件的人数
# for item in 'abcdefghji':#range while做一遍
#     age=int(input('同学，请问下你今年多大了？'))#转了整数
#     if 10<=age<=12:
#         sex=input('方便填写一下你的性别吗？')
#         if sex=='f':
#             print('恭喜你，满足条件，可以加入我们的女子足球队！')
#             count+=1#满足条件就+1
#         else:
#             print('很遗憾，你不能加入我们的足球队！再见！')
#     else:
#         print('很遗憾，你不能加入我们的足球队！再见！')
# print('满足条件的总人数是：{0}'.format(count))