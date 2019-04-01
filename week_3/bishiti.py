# -*- coding: utf-8 -*-
# 输入num为4位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第一位和第四位互换，第二位和第三位互换
3）最后合起来作为加密后的整数输出
a='q,w,e'
a1=a.split(',')
print(a1)
# >> image_list = image.strip(',').split(',')
b=a.strip('()').split(a)
print(b)

# c=['q', 'w', 'e']
c=[1,2,3,4,5,6]
d1=list(c)
d=d1[0:2]
print(d)
