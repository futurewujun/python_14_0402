# -*- coding: utf-8 -*-
# salary = int(input("请输入你的工资："))
# goods = {"001": ["手机", "1999"], "002": ["洗衣机", "2500"], "003": ["电饭煲", "1200"]}
# for i, j in goods.items():         # 把字典中每对key和value组成一个元组，并把这些元组放在列表中返回。
#     print("商品编号:" + i, j[0] + ":" + j[1])    #
# buy_goods=[]
# while 1:
#     choice_id = input("请输入要购买的商品编号：")
#     if salary > int(goods[choice_id][1]):       # 工资大于价格（价格取字典中列表下标 为1的值）
#         print("已成功支付！余额还有{}".format(salary-int(goods[choice_id][1])))
#         salary=salary-int(goods[choice_id][1])
#         buy_goods.append(goods[choice_id][0])
#     elif salary - int(goods[choice_id][1]) < int(goods[choice_id][1]):  # 若工资小于余额，就提示并退出
#         print("工资不足以支付该款商品")
#     out_or_no =input('现在结账(y)，继续购买(n):')
#
#     if out_or_no is 'y':
#         print('你购买的商品有：{}'.format(buy_goods))
#         break
#     else:
#         pass

# a = 'qw'
# b = 'qw'
# print(a != b)

# a='q,w,e,r,t,y,'
# a=a.strip(',')            # 删除前后的 ，
# print(a)

# b=['手机','冰箱']
# print(','.join(b))      # 转换成字符串

# a=[1,2,3]
# print(str(a).strip('[]'))    # 转换成字符串后，移除字符串头尾的 []

# a = [1,7,4,89,34,2]
# b = a.remove(1)         # 删除列表指定的元素
# a1 = a
# print(a1)

# temp=input('输入需要判断的年份：')
# while not temp.isdigit():
#     print("您的输入有误，请输入一个数字！")
#     temp=input()
# year=int(temp)
# i=year%400
# j=year%100
# if i==0 and j==0:
#     print(temp+'是闰年！')
# else:
#     print(temp+'是平年')

#
# a= '平价菜中的手撕包菜'
# index = a.index('中的')
# print(index)
# a1 = a[:index]
# a2 = a[index+2:]
# print(a1)
# print(a2)

# a=['q','w','r','e']
# b='{1,2,3,4,5}'
# if '{}' in b:
#     print('1')
# else:
#     print('2')

# a=input("请输入数据（多个数据以空格分隔）：").split(" ")
# if len(a)>2:print("列表长度大于2,前两个数据为：{},{}".format(a[0],a[1]))
# else:print("列表{}长度小于2".format(a))

a=list(input("请输入列表：").strip("[]"))
#print(a)
if len(a)>2:
    a.remove(",")
    #print(a)
    if len(a)>2:
        print("列表长度大于2,前两个数据为：{},{}".format(a[0],a[1]))
    else:
        print("列表{}长度小于2".format(a))
else:print("列表{}长度小于2".format(a))