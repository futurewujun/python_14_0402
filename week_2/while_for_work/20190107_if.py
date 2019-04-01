# -*-coding:utf-8-*-
# @Time      :2019/1/8/008 9:42
# @Author    :Tanxi
# @Email     :1410510771@qq.com
# @File      :20190107_if.py
# @Software  :PyCharm Community Edition

# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
#方法一：
score=input('请输入您的成绩：')
if score!='' :
    score=float(score)
    if score>=0 and score<=100:
        if score >= 90:
            print('成绩等级：优秀')
        elif score >= 80:
            print('成绩等级：良好')
        elif score >= 60:
            print('成绩等级：及格')
        else:
            print('成绩等级：不及格')
    else:
        print('您输入的成绩超出0~100的范围')
else:
    print('成绩输入不能为空')

#方法二：
score=input('请输入您的成绩：')
if score!='' :
    score=float(score)
    if score>=0 and score<=100:
        if score >= 90:
            print('成绩等级：优秀')
        if score >= 80:
            print('成绩等级：良好')
        if score >= 60:
            print('成绩等级：及格')
        if score < 60:
            print('成绩等级：不及格')
    else:
        print('您输入的成绩超出0~100的范围')
else:
    print('成绩输入不能为空')



#2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格#方法一：
#方法一：
selling_price=float(input('请输入您的购买金额：'))
if selling_price >= 50 and selling_price <= 100:
    final_price = selling_price*0.9
    print('您购买的商品最终价格有10%的折扣，最终价格为{}'.format(final_price))
elif selling_price > 100:
    final_price = selling_price*0.8
    print('您购买的商品最终价格有20%的折扣，最终价格为{}'.format(final_price))
elif selling_price > 0:
    final_price = selling_price
    print('您购买的商品最终价格未达到享受折扣要求，最终价格为{}'.format(final_price))
else:
    print('您输入的购买金额不正确，请重新输入！')

#方法二：
selling_price=float(input('请输入您的购买金额：'))
if selling_price >= 50 and selling_price <= 100:
    final_price = selling_price*0.9
    print('您购买的商品最终价格有10%的折扣，最终价格为{}'.format(final_price))
    if selling_price > 100:
        final_price = selling_price*0.8
        print('您购买的商品最终价格有20%的折扣，最终价格为{}'.format(final_price))
    if selling_price > 0:
        final_price = selling_price
        print('您购买的商品最终价格未达到享受折扣要求，最终价格为{}'.format(final_price))
else:
    print('您输入的购买金额不正确，请重新输入！')

#3、输入一个数，判断一个数n能同时被3和5整除
#方法一：
n = int(input('请输入一个整数：'))
if n%3 == 0 and n%5 ==0:
    print('{}可同时被3和5整除'.format(n))
else:
    print('{}不可同时被3和5整除'.format(n))

#方法二：
n = int(input('请输入一个整数：'))
if n%3 == 0:
        if n%5 ==0:
            print('{}可同时被3和5整除'.format(n))
else:
    print('{}不可同时被3和5整除'.format(n))

#4、输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年
#方法一：
year = int(input('请输入年份：'))
if year%4 == 0 and year%100 != 0:
    print('{}是普通闰年'.format(year))
elif year%400 == 0:
    print('{}年是世纪闰年'.format(year))
else:
    print('{}年不是闰年'.format(year))

#方法二：
year = int(input('请输入年份：'))
if year%400 == 0:
    print('{}年是世纪闰年'.format(year))
else:
    if year%4 == 0 and year%100 != 0:
        print('{}是普通闰年'.format(year))
    else:
        print('{}年不是闰年'.format(year))

#5、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
#方法一：
n = input('请输入一个5位整数：')
if len(n) == 5:
    if n[0] == n[-1] and n[1] == n[-2]:
        print('{}是回文数'.format(n))
    else:
        print('{}不是回文数'.format(n))
else:
    print('请输入5位整数')

#方法二：
n = int(input('请输入一个5位整数：'))
if len(n) == 5:
    i=0
    if i < 2:
        if n[i] == n[4-i]:
            i += 1
            print('{}是回文数'.format(n))
        else:
            print('{}不是回文数'.format(n))
else:
    print('请输入5位整数')

#6、生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal
#方法一：
import random
a = random.randint(1,9)
print('当前随机数为：',a)

b = float(input('请输入一个数字:'))
if b>a :
    print('bigger')
elif b<a :
    print('less')
else:
    print('equal')

#方法二：
import random
a = random.randint(1,9)
print('当前随机数为：',a)

b = float(input('请输入一个数字:'))
if b > a :
    print('bigger')
if b < a :
    print('less')
if b == a:
        print('equal')

#7、写一个餐厅菜单显示程序：（大概的设计模式如下） 请自己设计一个数据存储这些菜单，
# 然后根据你从客户端输入的数据去进行菜名的读取。
# pingjiacai = {'手撕包菜':'10','茄子豆角':10,'苦瓜炒蛋':'12',
#               '苦瓜炒肉':'12','农家小炒肉':'13',
#               '酸辣鸡杂':'15','土豆烧肉':'15',}
# liangcai = {'凉拌黄瓜':'8','凉拌皮蛋':'9'}
# xiaoguoxianchao = {'大盆花菜':'16','长豆角鲮鱼':'19','水煮鱼（小）':'15','水煮鱼（大）':'27','红烧鱼块':'18',
#                    '香煎鲫鱼':'21','嗦螺焖鸡':'18','水煮鸡':'26','拍辣椒排骨':'25','酸萝卜耳尖':'22'}
# menu = [pingjiacai,liangcai,xiaoguoxianchao]

#*******上述存储怎么取值？？*********

menu = {'平价菜':{'手撕包菜':'10','大白菜':'10','土豆丝':'10','炒莴笋':'10','上海青':'10','青椒炒茄子':'10','焖白豆腐':'10',
              '青椒香干':'10','茄子肉沫':'10','茄子豆角':'10','青椒油豆腐':'10','青椒炒蛋':'10','苦瓜炒蛋':'12',
              '苦瓜炒肉':'12','农家小炒肉':'13','四季豆炒肉':'13','拍辣椒皮蛋':'13','酸辣鸡杂':'15','土豆烧肉':'15',
              '土匪猪肝':'15','丝瓜焖荷包蛋':'15','干豆角炒鸡':'15'},
        '凉菜':{'凉拌黄瓜':'8','凉拌皮蛋':'9'},
        '小锅现炒':{'大盆花菜':'16','长豆角鲮鱼':'19','水煮鱼（小）':'15','水煮鱼（大）':'27','红烧鱼块':'18',
                   '香煎鲫鱼':'21','嗦螺焖鸡':'18','水煮鸡':'26','拍辣椒排骨':'25','酸萝卜耳尖':'22'}
        }

#方法一：
jclx = input('请输入菜单中点餐类型：')
if jclx in menu.keys():
    if jclx == '平价菜':
        order = input('请输入菜名：')
        if order in menu['平价菜']:
            print(order+':'+menu['平价菜'][order]+'元')
        else:
            print('平价菜中没有该道菜')
    elif jclx == '凉菜':
        order = input('请输入菜名：')
        if order in menu['凉菜']:
            print(order + ':' + menu['凉菜'][order]+'元')
        else:
            print('凉菜中没有该道菜')
    else:
        order = input('请输入菜名：')
        if order in menu['小锅现炒']:
            print(order + ':' + menu['小锅现炒'][order]+'元')
        else:
            print('小锅现炒中没有该道菜')
else:
    print('您输入的点餐类型有误！')

#方法二：
jclx = input('请输入菜单中点餐类型：')
if jclx in menu.keys():
    if jclx == '平价菜':
        order = input('请输入菜名：')
        if order in menu['平价菜']:
            print(order+':'+menu['平价菜'][order]+'元')
        else:
            print('平价菜中没有该道菜')
    if jclx == '凉菜':
        order = input('请输入菜名：')
        if order in menu['凉菜']:
            print(order + ':' + menu['凉菜'][order]+'元')
        else:
            print('凉菜中没有该道菜')
    if jclx == '小锅现炒':
        order = input('请输入菜名：')
        if order in menu['小锅现炒']:
            print(order + ':' + menu['小锅现炒'][order]+'元')
        else:
            print('小锅现炒中没有该道菜')
else:
    print('您输入的点餐类型有误！')





