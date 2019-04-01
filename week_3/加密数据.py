# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 21:51
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 加密数据.py
# 3、输入num为四位数，对其 按照 如下的规则 进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第1位和第4为互换，第二位和第三位互换
# 3）最后合起来作为加密后的整数输出: 作为一个字符串整体输出

def func():
    num=input('请输入4个数字')
    L=[]#存储数据
    for item in num:
        item=(int(item)+5)%10#取余运算 10%10
        L.append(item)
    L.reverse()#倒序一下
    print(L)
    s=''#空字符串
    for item in L:
        print(item)
        print('item的数据类型:',type(item))
        s+=str(item)#str() int() float() 强制转化
    print(int(s))

func()

#
# s=[1,2,3,4]
# s[0],s[3]=s[3],s[0]
# print(s)