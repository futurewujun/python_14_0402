# -*- coding: utf-8 -*-
# a = {'name':'w','age':10}
# print(type(a))
# for i in a:
#     print(i)

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
def join_team(sex,age,k=int(4),x=int(10),y=int(12)):
    sum=0        #人数
    count=0      #次数
    while 1:
        sex = input('性别是：')
        age = int(input('年龄是：'))
        if sex == 'f'  and x<=age<=y:
            print('恭喜加入球队')
            sum+=1
        else:
            print('抱歉不能加入球队')
        count+=1
        if count == k:
            break
    print('共有{}人加入球队。'.format(sum))
# sex1 = input('性别是：')
# age1 = int(input('年龄是：'))
join_team('sex','age')


# {'name':'qwe','age':'12'}
# ['q','w','e','r','t']


eqwda=-eqwdaasd大；。
def join_team(x,y,z,sex,k):
    sum = 0
    count = 0
    while 1:
        if x<=z<=y and sex == 'f':
            print('可以加入足球队。')
            sum+=1
        else:
            print('不可以加入足球队。')
            break
        count+=1
        if count == k:
            break

x1=input('最小年龄：')
y1=input('最大年龄：')
k1=input('询问次数：')
z1=input('年龄：')
sex1=input('性别：')
join_team(x1,y1,z1,sex1,k1)
