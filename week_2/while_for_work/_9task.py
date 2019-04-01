# -*- coding: utf-8 -*-
# 9:购物车程序 需求：
# 1：启动程序后，让用户在控制台输入工资，然后打印商品信息（随便你们自己用什么方式存储商品，记得要有商品的编号、名称以及价格）
# 2：允许用户根据商品编号购买商品
# 3：用户选择商品后，监测余额是否足够，如果足够就直接扣款，不够就提醒用户，不能购买这个商品。
# 4：可随时退出，退出后，打印已购买商品和余额
salary = int(input("请输入你的工资："))
print('商品信息：')
goods = {'001': ['手机', '1999'], '002': ['洗衣机', '1200'], '003': ['电饭煲', '500'],'004':['冰箱','998']}
for i, j in goods.items():         # 把字典中每对key和value组成一个元组，并把这些元组放在列表中返回。
    print( '商品编号:' + i + '\t', j[0] + ':' + j[1])
buy_goods = ''          # 存已经购买的商品
while 1:
    choice_id = input("请输入要购买的商品编号：")
    if choice_id in goods:
        if salary  >= int(goods[choice_id][1]):       # 工资大于价格（价格取字典中列表下标 为1的值）
            print("已成功购买{}！余额还有{}".format(goods[choice_id][0],salary-int(goods[choice_id][1])))
            salary=salary-int(goods[choice_id][1])    #  可用余额
            buy_goods += '、'  # 加、号隔开
            buy_goods=buy_goods+goods[choice_id][0]   # 将已买的商品加入到buy_goods 中
            buy_goods = buy_goods.strip('、')        # 去掉字符串首尾的 ' 、'
        elif salary-int(goods[choice_id][1]) < int(goods[choice_id][1]):    # 若工资余额小于价格，就提示并退出
            print('工资不足以支付该款商品！')
            break
        y_or_n =input('现在结账(y)，或输入任意内容继续购买:')    # 判断退出还是继续
        if y_or_n == 'y':
            break
    else:
        print('没有此商品')
print('你购买的商品有：{}；余额还有{}。'.format(buy_goods[:], salary))

