# -*- coding: utf-8 -*-

# 1.根据输入的数据，来判断学生的成绩。输入数据函数:input()
# # 一：if条件语句
# score = int(input('请输入分数：'))
# if score > 90:
#     print('优秀！')
# elif score > 80:
#     print('良好！')
# elif score > 60:
#     print('一般！')
# else:
#     print('还需努力啊！')
# # 二：嵌套
# score = int(input('请输入分数：'))
# if score > 90:
#     print('优秀！')
# else:
#     if score > 80:
#         print('良好！')
#     else:
#         if score > 60:
#             print('一般！')
#         else:
#             print('还需努力啊！')
#
# # 2.一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
# # 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
# # 一：if
# price = float(input('请问价格是：'))
# if 50<=price<=100:
#     print('{0}元的折扣是10%，最终价格是{1}元'.format(price,price-price*0.1))
# elif price>100:
#     print('{0}元的折扣是20%，最终价格是{1}元'.format(price,price-price*0.2))
# else:
#     print('不好意思，少于50元不打折！')
# # 二： (跟第一题类似)
# price = float(input('请问价格是：'))
# if 50<=price<=100:
#     print('{}元的折扣是10%，最终价格是{}元'.format(price,price*0.9))
# else:
#     if price>100:
#         print('{}元的折扣是20%，最终价格是{}元'.format(price,price*0.8))
#     else:
#         print('不好意思，少于50元不打折')
#
# # 三：
# def zhekou(price):    # 定义一个计算折扣的函数
#     if 50 <= price <= 100:
#         print('{}元的折扣是10%，最终价格是{}元'.format(price, price * 0.9))
#     else:
#         if price > 100:
#             print('{}元的折扣是20%，最终价格是{}元'.format(price, price * 0.8))
#         else:
#             print('不好意思，少于50元不打折！')
# h = float(input('请问价格是：'))
# zhekou(h)  # 调用函数
# # 3.输入一个数，判断一个数n能同时被3和5整除
# # # 一：if
# n = int(input('请输入一个数：'))
# if n%3 == 0 and n%5 == 0:
#     print('{}能同时被3和5整除。'.format(n))
# else:
#     print('{}不能同时被3和5整除。'.format(n))
# # 二：嵌套
# x = int(input('请输入一个数：'))
# if x%3 == 0:
#     if x%5 == 0:
#         print('{}能同时被3和5整除。'.format(x))
#     else:
#         print('{}不能同时被3和5整除。'.format(x))
# else:
#     print('{}不能同时被3和5整除。'.format(x))
# # 三：函数
# def judge(k):   #定义一个判断函数
#     if k % 3 == 0 and k % 5 == 0:
#         print('{}能同时被3和5整除。'.format(k))
#     else:
#         print('{}不能同时被3和5整除。'.format(k))
# e = int(input('请输入一个数：'))
# judge(e)       #引用函数
#
# # 4.输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年
# # # 一：if
# year = int(input('请输入一个年份：'))
# if year%4 == 0 and year%100 != 0 or year%400 == 0:
#     print('{}年是闰年'.format(year))
# else:
#     print("{}年不是闰年".format(year))
# # 二：
# year1 = int(input('请输入一个年份：'))
# if year1%4 == 0 and year1%100 != 0:
#     print('{}年是闰年'.format(year1))
# elif year1%400 == 0:
#     print('{}年是闰年'.format(year1))
# else:
#     print("{}年不是闰年".format(year1))
#
# # 5.一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
a = input('请输入一个五位数字：')
while not a.isdigit or len(a) != 5:           # 不是五位的数字就一直循环提示输出
    a = input('请输入一个五位数：')
if a[0] == a[-1] and a[1] == a[-2]:
    print('{}是回文数。'.format(a))
else:
    print('{}不是回文数。'.format(a))

# # 一:if
# a = input('请输入一个五位数:')
# if a.isdigit():
#     b = list(str(a))      # 转为列表前先转为字符串
#     if len(b) != 5:       # 判断b的长度
#         print('位数错误，重新输入')
#     elif b[0] == b[4] and b[1] == b[3]:
#         print('{}是回文数。'.format(a))
#     else:
#         print('{}不是回文数。'.format(a))
# else:
#     print('请输入五位整数')
# # 二：嵌套
# a1 = int(input('请输入一个五位数:'))
# if a1.isdigit():
#     b1 = list(str(a1))      # 转为列表前先转为字符串
#     if len(b1) != 5:       # 判断b的长度
#         print('位数错误，重新输入')
#     else:
#         if b1[0] == b1[4] and b1[1] == b1[3]:
#             print('{}是回文数'.format(a1))
#         else:
#             print('{}不是回文数。'.format(a))
# else:
#     print('请输入五位整数')
#
# # 6.生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal
# import random
# q = random.randint(1,9)    # 取1-9 的整数
# w = int(input('请输入一个数字：'))
# if w > q:
#     print('bigger')
# elif w < q:
#     print('less')
# else:
#     print('equal')
# # 二:嵌套
# import random
# q1 = random.randint(1,9)
# w1 = int(input('请输入一个数字：'))
# if w1 > q1:
#     print('bigger')
# else:
#     if w1 < q1:
#         print('less')
#     else:
#         print('equal')
#
# # # 7.写一个餐厅菜单显示程序：（大概的设计模式如下） 请自己设计一个数据存储这些菜单，然后根据你从客户端输入的数据去进行菜名的读取。
# menu = {'手撕包菜':'10元','苦瓜炒肉':'12元','土豆丝':'10元','木耳炒肉':'12元','凉拌皮蛋':'9元','水煮鱼':'27元',}
# d = input('请输入你想点的菜：')
# if d in menu.keys():    # 判断key是否存在d
#     print('{0}：{1}'.format(d,menu[d]))  # 格式化输出
# else:
#     print('没有这道菜哦。')
# # 二：将菜名单独再存一个列表（额，，为了加一种方法而写。复杂化了。平时不考虑）
# menu = {'手撕包菜':'10元','苦瓜炒肉':'12元','土豆丝':'10元','木耳炒肉':'12元','凉拌皮蛋':'9元','水煮鱼':'27元'}
# d = input('请输入你想点的菜：')
# z = []          # 创建一个空列表
# for i in menu.keys():     # 遍历key值
#     z.append(i)        # 将所遍历的值存入列表 z 中
# if d in z:         # 判断菜名是否存在
#     print('{}:{}'.format(d,menu[d]))   # 格式化输出
# else:
#     print('没有这道菜哦。')
# 再写一种方法#####################################################