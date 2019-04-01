# -*- coding: utf-8 -*-
# @Time     : 2019-1-1510:11
# @Author   : Luocq
# @Email    : 1102858803@qq.com
# @File     : class_0115_def.py
# @Software : PyCharm Community Edition

#进阶提升题：
'''
1：利用字符串所学内置函数，完成如下题目，具体使用的函数已经提示过了~在课堂上，请去视频里面找答案！
    请用自己目前所学实现指定字符串大写转小写，小写变大写，并且将字符串变为镜像字符串，
    镜像的意思是：大写的’A’变为’Z’,’大写的‘B‘变成‘Y,小写的’’’b’变为’y 。
    目前要求处理的示范字符串是： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa” 需要提供至少2种不同的解决方法。
'''
#法一：通过循环改变字符的大小，并对其进行镜像处理
def a(str):
    a = 'ABCDEFGHIJKMLMNOPQRSTUVWXYZ'
    b = 'abcdefghijkmlmnopqrstuvwxyz'
    new_str = ''
    for i in range(len(str)):
        if str[i].isupper():#判断字符是否是大写
            c = str[i].lower()#将大写字符转换成小写
            index = 26 - b.find(c)#找到此目标字符在小写的字符串b中的索引值，并找到其镜像字符的索引值
            new_str = new_str + b[index]#取出目标字符在字符串b中的镜像字符，并将其添加到新的字符串中
        elif str[i].islower():#判断字符是否是小写
            c = str[i].upper()#将小写字符转换成大写
            index = 26 - a.index(c)#找到此目标字符在大写的字符串a中的索引值，并找到其镜像字符的索引值
            new_str = new_str + a[index]#取出目标字符在字符串a中的镜像字符，并将其添加到新的字符串中
    return new_str#将获取到的结果返回
#法二：通过swapcase()改变字符的大小，再通过循环对其进行镜像处理
def b(str):
    a = 'ABCDEFGHIJKMLMNOPQRSTUVWXYZ'
    b = 'abcdefghijkmlmnopqrstuvwxyz'
    new_str = ''
    str = str.swapcase()  # 将字符串的大小写互相转换
    for i in str:
        if i.isupper():  # 判断字符是否是大写
            index = 26 - a.index(i)  # 找到此目标字符在大写的字符串a中的索引值，并找到其镜像字符的索引值
            new_str = new_str + a[index]  # 取出目标字符在字符串a中的镜像字符，并将其添加到新的字符串中
        elif i.islower():  # 判断字符是否是小写
            index = 26 - b.index(i)  # 找到此目标字符在小写的字符串b中的索引值，并找到其镜像字符的索引值
            new_str = new_str + b[index]  # 取出目标字符在字符串b中的镜像字符，并将其添加到新的字符串中
    return new_str #返回结果
# 法三：通过ASCII编码
def c(str):
    new_str = ""
    for i in str:
        index = 187 - ord(i)  # 找到此字符的ASCII编码，再找到对应的小/大写字母的镜像字母的ASCII编码
        i = chr(index)  # 将找到的ASCII编码转换为字母
        new_str = new_str + i #将最后的结果添加到新的字符串中
    return new_str #返回结果
# 法四：通过maketrans()对其进行大小转换和镜像处理利用
def d(str):
    new_str = ""
    for i in str:
        a = chr(187 -ord(i)) # 找到目标字母的镜像字母的ASCII编码，并转换为字母
        j = str.maketrans(i, a) # 生成对应的转换表
        i = chr(j[ord(i)]) #获取转换后的对应字母
        new_str = new_str + i #将最后的结果添加到新的字符串中
    return new_str #返回结果
str = "sdSdsfdAdsdsdfsfdsdASDSDFDSFa"
print(a(str))
print(b(str))
print(c(str))
print(d(str))

'''
2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
    比如这个字符串： 我的是名字是lemon,今年5岁。
    语法分析后得到结果如下：
        数字：5
        中文：我的名字是、今年、岁
        拼音：lemon
        符号：，。
    请编写程序实现该词法分析功能。
'''
import re
def morpheme_analysis():
    str = input("请输入数据：")
    sz_num = re.findall(r'(\d+)', str)#正则表达式提取数字

    regex = re.compile("[\u4e00-\u9fa5]+")#将字符串转为中文的编码格式
    ch_num = regex.findall(str) #正则表达式提取中文

    py_num = re.findall(r'[A-Za-z]+', str) #正则表达式提取字母

    #正则表达式提取符号
    zf_num = re.findall(r'[\,\.\/\;\:\?\>\<\"\'\[\]\{\}\-\_\=\+\|\\\(\)\*\&\^\%\$\#\@\!\~\`\，\。\、\？\》\《\：\；\“\”\‘\’\{\}\【\】\|\、\+\=\—\—\-\（\）\*\&\……\%\￥\#\@\！\~\·\ ]+', str)

    print('''
        语法分析后得到结果如下：
                数字：{}
                中文：{}
                拼音：{}
                符号：{}
        '''.format(sz_num, ch_num, py_num, zf_num))  # 返回结果
morpheme_analysis()

##新手练习题：
#1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def object_len(a):
    if len(a) > 5:#判断传入对象的长度是否大于5
        print("%s的长度大于5"%a) #返回判断的结果
    elif len(a) < 5:#判断传入对象的长度是否小于5
        print("%s的长度小于5"%a)#返回判断的结果
    else:#判断传入对象的长度是否等于5
        print("%s的长度等于5"%a)#返回判断的结果
object_len("sdfrvdea")

#2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def check_len(list):
    if len(list)>2:#判断列表长度是否大于2
        list = list[0:2]#切片获取前两个长度
    return list#返回新的列表
list = [1,2,3,4,5,6,7]
print(check_len(list))

#3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
def add_str(a,dict):
    if a not in dict:#判断字符串是否存在与字典中，不存在继续下一步
        dict[a] = a#将字符串添加到字典中，key,value的值相同
    return dict#返回最后的字典
dict = {}
print(add_str("abc",dict))

'''
4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
'''
def select_girl(x,y,k):
    count = 1
    sum_f = 0
    while count <= k:
        sex = input("请输入小孩的性别（f为男，m为女）：")#获取输入的小孩性别
        if sex == "m" or sex == "女":#判断输入的性别是否为女
            while True:
                age = input("请输入小孩的年龄：")#获取输入的小孩年龄
                if age.isdigit():#判断输入的年龄是否为数字
                    age = int(age)#将输入的字符串转为int类型
                    if age >= x and age <= y:#判断输入的年龄是否符合要求，在x~y之间
                        sum_f = sum_f + 1#满足条件的人数+1
                        print("此小孩符合要求，可以加入球队！")
                        break#满足条件，退出循环
                    else:
                        print("此小孩不符合要求，不可以加入球队！")
        elif sex == "f" or sex == "男":
            print("此小孩不符合要求，不可以加入球队！")
        else:
            print("请输入小孩的性别，如:男（或f），女（或m）。")
        count = count + 1
    print("询问了{}个小孩，有{}个小孩可以加入".format(k,sum_f))#返回最后的结果
select_girl(10,12,10)