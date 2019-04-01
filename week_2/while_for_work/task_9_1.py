# # -*- coding: utf-8 -*-
salary = int(input("请输入你的工资："))
goods = {"001": ["手机", 1999], "002": ["洗衣机", 1200], "003": ["电饭煲", 500], "004": ["冰箱", 998]}
for i, j in goods.items():  # 把字典中每对key和value组成一个元组，并把这些元组放在列表中返回。
    print("商品编号:" + i + "\t", j[0] + ":" + str(j[1]))
buy_goods = []
y_or_no = 'y'
while y_or_no == 'y':
    chioce = input("请输入你要购买的商品编号：")
    if chioce in goods:
        if salary > goods[chioce][1]:
            buy_goods.append(goods[chioce][0])
            salary -= goods[chioce][1]
            print("成功购买{},工资余额：{}元".format(goods[chioce][0], salary))
        else:
            print("您的工资不足以支付该商品！")
        y_or_no = input("继续购买（y）,结束购买（任意按键）:")
        if y_or_no != "y":
            print("退出购物系统！,感谢您的使用")
    else:
        print("输入错误,库存中没有您要购买的商品！")
if buy_goods == None:
    print("感谢试用购物系统，您本次未购买商品！")
else:
    print('你本次购买的商品有：%s；余额还有{}元'.format(str(buy_goods[:]).strip('[]'), salary))
