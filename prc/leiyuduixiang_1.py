# -*- coding: utf-8 -*-
import random
class caiquan():
    def __init__(self):
        self.user_win = 0
        self.com_win = 0
        self.pingju = 0

    def choice(self):
        self.juese = int(input("请输入数字选择角色\n1.曹操   2.张飞    3.刘备\n:"))

    def wanjia(self):
        self.user_cq = int(input("请输入数字：\n1.剪刀    2.石头    3.布\n"))
        self.diannao()
        return self.ch

    def diannao(self):  # 1.剪刀    2.石头    3.布
        self.com_cq = random.randint(1, 3)
        self.reult()

    def reult(self):
        if self.user_cq == self.com_cq:
            print("玩家选择：", self.user_cq, "电脑选择：", self.com_cq)
            print("平局")
            self.pingju += 1
        elif (self.user_cq == 1 and self.com_cq == 2) or (self.user_cq == 2 and self.com_cq == 3) or (
                self.user_cq == 3 and self.com_cq == 1):
            print("玩家选择：", self.user_cq, "电脑选择：", self.com_cq)
            print("电脑赢！")
            self.com_win += 1
        else:
            print("玩家选择：", self.user_cq, "电脑选择：", self.com_cq)
            print("玩家赢！")
            self.user_win += 1
        self.ch = input("\n是否继续（y or n）：")

game = caiquan()
game.choice()
ch = 'y'
while ch == 'y':
    ch = game.wanjia()

print("玩家赢：{}次,电脑赢：{}次,平局：{}次".format(game.user_win, game.com_win, game.pingju))
