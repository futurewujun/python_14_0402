# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 11:08
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_函数的概念.py

#函数的定义：实现某个指定的功能  重复使用
# type()
# len()
# range()
#函数有啥作用:提高代码的复用性

#函数的语法：关键 def 顶格写
#函数的具体语法：请自动copy到你的脑子里面
# def 函数名(参数1,参数2,参数3):
   #函数体：本函数要实现的功能
   #return 表达式

#def 顶格写 表示这个是一个函数
# 函数名 小写 不同的字母与数字之间用下划线隔开  不能用数字开头
# 参数的个数可以大于等于0
# 函数体是函数的子代码  要有缩进  写自己想实现的功能即可
# return后面的表达式 >=0个
# == 1个    返回你指定的数据类型
# >1        返回的是元组类型，用逗号区分
# == 0个    返回None
#return的作用 就是当你调用函数的时候  会返回return后面的表达式的值
#如果你的return后面没有表达式  写没写 没有区别

#如何调用函数  函数名(对应个数的参数)
#None 没有返回任何东西 空的

# def radio_machine():
#     print('就是一个复读机，只会说：你好！！！')
#     return [1,2,3,4],['666','hello']#隐式的添加一个return

def add():
    result=8+8
    print(result)
    return result

# 请你拿到add()运行的求和结果 再去加20  再输出到控制台
# print(add())
res=add()+1
print(res)

# res=radio_machine()#存储返回的值
# print('函数的返回值是:{}'.format(res))
#函数里面 return的表达式个数
#==1 返回你指定的数据利息
#>1  返回的是元组类型
#==0 返回None