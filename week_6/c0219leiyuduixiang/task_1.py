# -*- coding: utf-8 -*-
# 1：人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1曹操 2张飞 3刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random
class MoraGame:
    '''人机猜拳游戏'''
    def __init__(self):
        self.fist = {'1':'剪刀', '2':'石头', '3':'布'}
    def choice_role(self):
        a = {'1':'曹操', '2':'张飞', '3':'刘备'}  # 角色
        print('---1:曹操，2:张飞，3:刘备---')
        while True:
            self.people = input('请输入对应数字选择你的角色：')
            if self.people in a.keys():
                print('你的角色是：{}'.format(a[self.people]))
                break
            else:
                print('请输入正确的数字。')

    def people_action(self):
        print('---1:剪刀，2:石头，3:b布---')
        while True:
            self.peo = input('请输入对应数字出拳：')     # 其他函数也能引用此变量
            if self.peo in self.fist.keys():
                peo_1 = self.fist[self.peo]  # 玩家的出拳
                print('玩家的出拳是：',peo_1)
                break
            else:
                print('请输入正确的数字。')

    def computer_action(self):
        self.com = random.randint(1,3)      # 其他函数也能引用此变量
        com_1 = self.fist[str(self.com)]  # 电脑的出拳,要将传入的随机数转成字符串类型
        print('电脑的出拳是：{}'.format(com_1))

    def battle(self):
        sum = 0     # 总局数，初始为0，
        sum_1 = 0   # 玩家赢的次数
        sum_2 = 0   # 电脑赢的次数
        sum_3 = 0   # 平局的次数
        res.choice_role()  # 选角色
        while 1:
            res.people_action() # 玩家出拳
            res.computer_action()   # 电脑出拳
            if  int(self.peo) == int(self.com):
                print('平局')
                sum_3 += 1
            elif (int(self.peo) == 1 and int(self.com) == 2) or (int(self.peo) == 2 and int(self.com) == 3) or (int(self.peo) == 3 and int(self.com) == 1):
            # elif int(self.peo) - int(self.com) in (-1,2)    # 或者这样判断
                print('电脑胜')
                sum_2 += 1
            elif (int(self.peo) == 1 and int(self.com) == 3) or (int(self.peo) == 2 and int(self.com) == 1) or (int(self.peo) == 3 and int(self.com) == 2):
            # elif int(self.peo) - int(self.com) in (-2,1)    # 或者这样判断
                print('玩家胜')
                sum_1 += 1
            # 先算总局数，再判断是否继续
            sum += 1

            while True:
                go_on = input('是否继续？(按y继续，按n 退出)')
                if go_on == 'n':
                    # flag = 1 # 标记为退出状态
                    break
                elif go_on == 'y':
                    # flag = 2 # 标记为继续状态
                    break
                else:
                    print('请输入正确选项。')
            if go_on == 'y':
                continue
            else:
                break
        print('一共玩了{}局，玩家赢了{}局，电脑赢了{}局，平局{}次，游戏结束。'.format(sum,sum_1,sum_2,sum_3))
res = MoraGame()
res.battle()

# 2：编写一个类：你们自行去设计，要求写一个类， 初始化函数 对象函数 包含 根据你不同的选择完成get请求 OR post请求，
# 其中url 需要做参数化，并且最后要拿到响应结果
'''import requests
class HttpRequest:
    def __init__(self,url):
        self.url = url  # 请求的url地址
    def get(self):
        res = requests.get(self.url)
        print('正在发起get请求')
        print(res.text)
    def post(self):
        res = requests.post(self.url)
        print('正在发起get请求')
        print(res.text)
res1=HttpRequest('http://www.baidu.com')
res1.get()
res1.post()
'''




