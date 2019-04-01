# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 20:40
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : if条件语句.py

#强制同学们选一个
#酸的A  甜的B  辣的C  苦的D  不知道自己的口味E

#明星
# A 周杰伦粉丝会
# B 彭于晏粉丝会
# C 胡歌粉丝会
# D 华华粉丝会
# E 无组织人员
#分支引流的作用

#条件判断 根据条件去进行判断去进行处理
#圣诞节来了
#心仪的对象表白  A 巧克力+鲜花  B 平安果

#条件语句 if ...else
#语法：
#if 条件表达式:#一般逻辑运算 比较运算 成员运算
    #代码
#else:
   #代码

# gift='鲜花'#条件
# if False:#代表我们下面有子代码  要缩进
#     print('表白成功，明天可以手牵手吃饭啦！')
# elif gift=='鲜花':
#     print('表白成功，明天可以手牵手看电影！')
# else:
#     print('表白失败！！！继续单身汪。')

#1：if elif 必须要加条件表达式 else不能加任何条件
#2： 什么情况才会执行if  elif的子代码？？？ 只有当条件满足  为True
#3: 非0 和非空的数据表示True  为0和为空的数据 表示False（非常重要)
#只要返回值是True 或者是False 都可以作为if 或者elif 后面的条件表达式

#小练习：从控制台获取一个成绩 根据成绩判断
# 如果 >80 优秀  >70 良好  >=60及格  <60 不及格
#数据的范围是0-100
score=input('请输入你的成绩：')#利用input从控制台获取的数据都是字符串类型的
if score.isdigit():
    score=int(score)
    if score>100 or score<0:
        print('数据范围应该在0-100之间')
    elif score>80:
        print('优秀')
    elif score>70:
        print('良好')
    elif score>=60:
        print('及格')
    else:
        print('不及格')
else:
    print('数据输入有误')