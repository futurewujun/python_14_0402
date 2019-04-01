# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 9:33
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_str.py

#字符串  str
a='hello python13y'

#1：常规用法：字符串的取值和切片
#1）字符串里面元素：单个字符算一个元素（数字 字母 符号 中文）
#2）统计字符串的长度：len(a)
print(len(a))
#3）如何取值：字符串取值是根据索引来的  索引是什么呢？ 是字符串元素的编号
#编号是从0开始的  取值方式：变量名[索引]
print(a[6])
print(a[-1])
print(a[0])

#3)切片:用法 变量名[m:n:k]# m 开始取值的索引位置  n取值结束的位置，取值不包含  k步长
#取左不取右 取到 n-1
print(a[0:15:2])#0 2 4 6 8 10 12

# 请把a字符串里面编号为偶数的元素用切片 打印出来
# print(a[::2])

#请把a字符串利用切片实现倒序输出  y31nohtyp olleh
print(a[14::-1])#14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
print(a[::-1])#-1 -2 -3 -4 -5。。。
print(a[-1:-16:-1])

#字符串的拼接 +  ,
s_1='hello'
s_2='卡哇伊'
a=20# 转成字符串 str()强制转化
print(s_1+s_2+str(a))
print(1,2,3,4,5)
#格式化输出
age=18
height=170.56
hobby='打篮球'

'''#格式化输出方法一 占坑符  %d %f %s 万能的是%s'''
print('''--------小CC的个人绝密档案----------
      年龄是：%s
      身高是：%0.1f
      业余爱好是:%s'''%(age,height,hobby))

#格式化输出方法二 {}
print('''--------Bay max的个人绝密档案----------
      年龄是：{1}
      身高是：{0}
      业余爱好是:{2}'''.format(height,age,hobby))#0开始编号坑 开始编号我们的元素
# print("hello",'world',1,0.02)

#函数
a='hEllo pYthOn13y'
# 切换大小写 upper() lower()  swapcase()
print(a.swapcase())

#replace 替换的方法  返回值
s=a.replace('l','@')
print(s)

'''# find 查找元素  没有找到就返回-1  只考虑正序 不考虑反序 -1'''
print(a.find('th'))#单个字符如果找到了 返回的是遇到的第一个元素的索引的值
#子字符串  长度大于1  如果找到了 就返回子字符串所在字符串里面第一个元素的位置
b='1sqwe'
print(b.isdigit())  # 判断是否全由整数构成
print(a[1].islower())#False
print(a[1].isupper())#True
print('@'.join(b))#h@E@l@l@o@ @p@Y@t@h@O@n@1@3@y  --- 将 @ 加到b里面

a='hEllo pYthOnh13y'
print(a.split('h'))#切割  返回的是列表，---从h两边切
# #布尔值  True False

#下节课
#周二  列表 字典 元组
#周四： if 与循环 循环是最难的！！！---重新做社区的作业
#周六：函数 也是最难的