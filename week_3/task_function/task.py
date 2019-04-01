# -*- coding: utf-8 -*-
# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def judge_length(a):
#     if '(' in a or ')' in a and '{' in a or '}' in a:    # 判断是否为字符串或列表的样式
#         n = list(a.strip('()[]').split(','))    # 去除首尾的()[]后再通过"，"对字符串切片再转成列表n
#         if len(n) > 5:
#             print('你传入的对象长度大于5')
#         else:
#             print('你传入的对象长度小于5')
#     else:
#         if len(a) > 5:
#             print('你传入的对象长度大于5。')
#         else:
#             print('你传入的对象长度不大于5。')
# a = input('请输入你要传入的对象：')
# judge_length(a)

# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# def judge_length(h):
#     if '[' not in h:
#         print('请输入列表格式')
#     else:
#         b=list(h.strip('[]').split(','))     # 转为列表b
#         if len(b)>2:
#             print('{}的前两个长度是：{}'.format(h,b[0:2]))
# temp = input('请输入列表：')
# judge_length(temp)

# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
# def judge_exist(d,s):       # d 为字典，s为字符串
#     if '{' in d and '}' in d:
#         d1 = eval(d)        # 转为字典
#         if s not in d1.values():    # 判断字符串是否存在于值
#             d1['new']=s
#             d2=d1
#             print('{}不为字典中的值，新的字典为：{}'.format(s,d2))
#         else:
#             print('所输入的字符串为字典中的值。')
#     else:
#         print('请输入正确的字典格式！')
#     return d
# a=input('请输入一个字典：')
# b=input('请输入字符串：')
# print(judge_exist(a,b))

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
def join_team(sex,age,k=int(3),x=int(10),y=int(12)):
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
join_team('sex','age')

# 1：利用字符串所学内置函数，完成如下题目，具体使用的函数已经提示过了~在课堂上，请去视频里面找答案！
# 请用自己目前所学实现指定字符串大写转小写，小写变大写，并且将字符串变为镜像字符串，镜像的意思是：大写的’A’变为’Z’,’
# 大写的‘B‘变成‘Y,小写的’’’b’变为’y 。目前要求处理的示范字符串是： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa” 需要提供至少2种不同的解决方法。
s='adSdsfdAdsdsdfsfdsdASDSDFDSFa'
s1=s.swapcase()     # 小写变大写，大写变小写
print(s.swapcase())
new_s1=''
for i in s1:
    if i.islower():
        i = chr(219-ord(i))     # 第一个小写字母与最后一个小写字母的ASCII之和为219
        # print(chr(97))
        # print(ord(i))
        # print(i)
        new_s1+=i
    elif i.isupper():
        i = chr(155-ord(i))     # 第一个大写字母与最后一个大写字母的ASCII之和为155
        new_s1+=i
print(new_s1)

# 2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串： 我的名字是lemon,今年5岁。 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。
s=input('请输入字符串：')
s_1=''
s_2=''
s_3=''
s_4=''
for i in s:
    # print(i)
    if ord(i) in range(48,58):
        s_1+=i
    if ord(i) in range(65,66) or ord(i) in range(97,123):
        s_2 += i
    if ord(i) in range(33,48) or ord(i) in range(58,65) or ord(i) in range(91,97):
        s_3 += i
    else:
        s_4 += i
print('数字：',s_1)
print('字母：',s_2)
print('符号：',s_3)
print('中文：',s_4)