# -*- coding: utf-8 -*-

import random
class MoraGame:
    '''人机猜拳游戏'''
    def choice_role(self):
        a = {1:'曹操', 2:'张飞', 3:'刘备'}  # 角色
        print('---1:曹操，2:张飞，3:刘备---')
        people = input('请输入对应数字选择你的角色：')
        print('你的角色是：'.format(a[people]))
    def people_action(self):
        b = {1:'剪刀', 2:'石头', 3:'布'}
        print('---1:剪刀，2:石头，3:b布---')
        peo = input('请输入对应数字出拳：')
        peo_1 = b[peo]  # 玩家的出拳
    def computer_action(self):
        c = {1: '剪刀', 2: '石头', 3: '布'}
        com = random.randint(1,3)
        com_1 = c[com]  # 电脑的出拳

    def battle(self):
        res.choice_role()
        res.people_action()
        res.computer_action()

res = MoraGam
print(res.battle())

