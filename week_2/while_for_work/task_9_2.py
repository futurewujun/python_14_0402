# -*- coding: utf-8 -*-
i = 0
tag = 1
# 定义一个空列表，用来存放购买的商品
buy_list = []
# 定义的一个空字典，通过键值对存放购买相同商品的数量
buy_dict = {}
product = [['product0001', '500'], ['product0002', '1000'],
           ['product0003',  '2000'], ['product0004', '800']]
while True:
    salary = input('请输入您的工资(元):')
    if salary.isdigit():
        salary = int(salary)
        while True:
            print("商城的商品列表如下：")
            for item in product:
                print('商品编号:{},商品名称:{},商品单价:{}'.format(i, item[0], item[1]))
                i += 1
            while int(tag):
                code_choice = input('请输入您需要购买的商品编号:')
                if code_choice.isdigit():
                    code_choice = int(code_choice)
                    if 0 <= code_choice <= len(product):
                        product_son = product[code_choice]
                        num = input('请输入您需要购买此商品的数量：')
                        if num.isdigit():
                            num = int(num)
                            price = int(product_son[1])
                            if salary >= price * num:
                                print('购买成功,账户余额为{}'.format(salary-price * num))
                                for i in range(num):
                                    buy_list.append(product_son[0])
                                salary -= price * num
                                while True:
                                    is_leave = input('您是否结束本次shopping(0表示离开,其他数字表示继续)：')
                                    if is_leave.isdigit():
                                        tag = int(is_leave)
                                        break
                                    else:
                                        print('请输入正确的结束数字！')
                                        continue
                            else:
                                print('对不起,购买此商品需要金额{}元，您的工资余额为{}元,余额不足!'.format(price * num, salary))
                                is_leave = input('是否结束本次购买？(1表示继续；0表示退出)：')
                                tag = int(is_leave)
                                continue
                        else:
                                print('请输入正确格式的商品数量！')
                else:
                    print('请输入数字形式的商品编号！')
            if len(buy_list) == 0:
                print('您本次未购买任何商品，欢迎下次光临！！')
            else:
                print("本次购物您购买了如下商品：")
                # 统计购买相同商品的数量
                for n in buy_list:
                    if buy_list.count(n) >= 1:
                        buy_dict[n] = buy_list.count(n)
                for m in buy_dict:
                    print('{}个{}'.format(buy_dict[m], m), end=';  ')
                print()
                print('''账户余额为{},欢迎下次光临!!!'''.format(salary))
            break
    else:
        print('请输入正确工资格式！')
        continue
    break