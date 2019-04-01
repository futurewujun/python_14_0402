# -*- coding: utf-8 -*-

'''
1.正则表达式：编写一些规范查找需要的字符串
2.正则表达式的组成：原义字符 和 原字符
3.如何用python来解析：re 模块
match()   从字符串开头位置开始匹配，开头由就返回，没有就返回None
search()  对字符串的任意位置进行匹配，找到一个就返回
findall() 返回字符串中所有匹配的字符串组成的一个列表
finditer()  返回一个包含了所有的匹配对象的迭代器

4.正则表达式的场景：
--- 参数化
--- 查找一些特殊的字符格式：邮箱，手机号码，身份证号码。。
元字符： . 匹配规则：可以匹配任意单个字符，汉字，字母，符号，数字（注意是单个，也就是一个）
\d ：匹配任意单个数字
限定符： + 匹配次数：至少匹配一次
？  ： 最多匹配一次
*   ： 匹配0次或者多次
'''
import re
tar="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
tar1='mobilephone'
# 原义字符的查找，根据正则表达式来查找，有匹配的字符串就返回一个对象
p='normal_user'
p1='mobile'
p2='#(.*?)#'   #（） 圆括号代表正则表达式里 组的概念
m=re.search(p2,tar) #任意位置找
print('m',m)
a=m.group() #不传参的时候返回表达式和匹配的字符串一起
c=m.group(1) #取到目标字符串 --- 传参就是指返回匹配的字符串，也就是当前租的匹配字符
print(c)
print(re.match(pattern=p1,string=tar1)) # 在最开始位置找，找不到返回None
b=re.findall(p2,tar)    #findall 找到所有的匹配的字符，返回的是一个列表
print(b)
tar2=re.sub(p2,'135123456',tar,count=1)    #查找并且替换,count=1：只替换第一个，默认为0是替换全部
print(tar2)

mn="{'mobilephone':'18688775656','pwd':'12345121216'}"
res=re.findall(pattern='\d{11}',string=mn)
# print(res)

