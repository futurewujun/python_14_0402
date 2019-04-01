# 新手练习题：
# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def object_length(a):
    """判断对象的长度是否大于5，是返回True，反之返回False"""
    # 判断传入的对象是否时str、list、tuple之一
    if isinstance(a, str) or isinstance(a, list) or isinstance(a, tuple):  # 判断对象是否是一个已知的类型
        if len(a) > 5:
            return True
        else:
            return False
    else:
        return "您传入的对象类型不在判断范围内，请重新传入！"
print(object_length(('q','w','e','a','s','d')))
# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# 方法一
def intercept_list(a):
    """返回列表前两个长度的内容"""
    # 定义一个空列表用来存储新的内容
    new_list = []
    if isinstance(a, list):
        if len(a) > 2:
            # ；利用for循环，将a的前两个长度的内容添加到new_list中，并返回new_list的值
            for item in range(2):
                new_list.append(a[item])
            return new_list
        else:
            return '列表的长度应大于2，请重新传入'
    else:
        return '请传入列表类型的参数！'

# 方法二
def intercept_list_2(a):
    """返回列表前两个长度的内容"""
    if isinstance(a, list):
        if len(a) > 2:
            # ；利用切片方法
            return a[0:2]
        else:
            return '列表的长度应大于2，请重新传入'
    else:
        return '请传入列表类型的参数！'

# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
def str_add_dict(a, b):
    """
    将字符串添加到列表中
    :param a: 字典对象
    :param b: 字符串对象
    :return:  一个新的字典
    """
    if isinstance(a, dict) and isinstance(b, str):
        # b不在列表a的之中,添加到a中
        if b not in a.values():
            a[b] = b
            return a
        else:
            return 'Error:字典中存在字符串的值,添加失败!!'
    else:
        return 'Error：请传入字典和字符串对象！！'

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。

def input_info():
    """
    接收用户数数输入的年龄和性别
    :return: 以数组的形式返回接收到的值
    """
    while True:
        age = input("请输入您的年龄:")
        if age.isdigit():
            age = int(age)
            sex = input('请输入您的性别(m表示男性，f表示女性):')
            # 返回值以数组的形式输出
            return age, sex
        else:
            print('请输入正确的年龄')
            continue

def find_player(x, y, k):
    """
    判断人员是否可以加入足球对
    :param x: 足球队年龄的下限
    :param y: 足球队年龄的上限
    :param k: 询问的人数/次数
    :return:  满足条件人的数量
    """
    num = 0
    for item in range(k):
        # 定义变量t接受函数input_info()的返回值
        t = input_info()
        if x <= t[0] <= y and t[1] == 'f':
            print("恭喜，您满足加入足球对的条件")
            # 满足条件人数自增1
            num += 1
        else:
            print('sorry,您不满足加入足球对的条件！！')
    return '本次询问,满足参加足球对条件的共有 {} 人'.format(num)
# --------------------------------------------------------------------------------------------------
# 进阶提升题：
# 1：利用字符串所学内置函数，完成如下题目，具体使用的函数已经提示过了~在课堂上，请去视频里面找答案！
# 请用自己目前所学实现指定字符串大写转小写，小写变大写，并且将字符串变为镜像字符串。
# 镜像的意思是：大写的’A’变为’Z’,’大写的‘B‘变成‘Y,小写的’b’变为’y'。
# 目前要求处理的示范字符串是： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”
# 需要提供至少2种不同的解决方法。

# 方法一：利用ASCII码值取转换  A=65  a=97   B=66  b=98 .....Y=89 y=121   Z=90  z=122
"""
分析：
可以看出ASCII值的相加 A+Z = B+Y = C+X = 155
                   a+z = b+y = c+z = 219
                   a-A = b-B = c-C =32
chr()   根据ASCII码获取对应的字符
ord()   根据字符获取ASCII值
"""
def str_mirror(s):
    """
    将字符串大小写转换，并镜像输出
    :param s: 字符串对象
    :return:  转换后的新字符串
    """
    # 定义一个空字符串用来接收转换后的值
    new_s = ''
    for item in s:
        # 判断如果是大写
        if item.isupper():
            # 将大写转换为小写
            swap_s1 = chr(ord(item) + 32)
            # 转换为小写的镜像
            swap_s1 = chr(219 - ord(swap_s1))
            # 利用字符串拼接输出
            new_s += swap_s1
        elif item.islower():
            # 将小写转换为大写
            swap_s2 = chr(ord(item) - 32)
            # 转换为大写的镜像
            swap_s2 = chr(155 - ord(swap_s2))
            new_s += swap_s2
    return '新的字符串为:{}'.format(new_s)


# 方法二：
"""
分析：字符串的两个内置函数
maketrans()：返回一个可用于str.translate()的翻译表
            如果有两个参数，它们必须是长度相等的字符串，并且在生成的字典中，x中的每个字符将映射到字符在y中的相同位置
translate() ：使用给定的转换表替换字符串中的每个字符。   """
def str_mirror_2(s):
    """     将字符串大小写转换，并镜像输出
            param s: 字符串对象
            return:  转换后的新字符串   """
    # 定义两个,作为maketrans()的两个参数
    s1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s2 = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
    # 返回的是一个翻译表，s1中的每个字符的ASCII值和s2对应位置上字符的ASCII值一一对应，并赋值给tanslate_table
    tanslate_table = s.maketrans(s1, s2)
    swap_s = s.swapcase()   # 转换大小写
    new_s = swap_s.translate(tanslate_table)    # 根据翻译表中成对的ASCII值，利用translate替换成对应的字符
    return new_s


# 2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串： 我的是名字是lemon,今年5岁。 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。
# 请编写程序实现该词法分析功能
def split_str(s):
    """按类别打印出字符串中的元素"""
    ch, digit, en, symbol = '', '', '', ''
    # 定义一个变量i,作为s的索引
    i = 0
    for item in s:
        # 判断是否为中文
        if u'\u4e00' <= item <= u'\u9fff':      # \u 应该代表为Unicode编码，中文的正则表达式
            # 判断item的下一个元素是否为中文
            if u'\u4e00' <= s[i+1] <= u'\u9fff':
                ch += item
                i += 1
            else:
                ch = ch+item+'、'
                i += 1
        # 判断是否为字母 字母的ASCII值在65-90 或者 97-122之间
        elif 65 <= ord(item) <= 90 or 97 <= ord(item) <= 122:
            if 65 <= ord(s[i + 1]) <= 90 or 97 <= ord(s[i + 1]) <= 122:
                en = en + item
                i += 1
            else:
                en = en + item + '、'
                i += 1
        # 判断是否为数字
        elif item.isdigit():
            if s[i+1].isdigit():
                digit += item
                i += 1
            else:
                digit = digit+item+'、'
                i += 1
        else:
                symbol += item
                i += 1
    print('数字：{}'.format(digit.strip('、')))
    print('中文：{}'.format(ch.strip('、')))
    print('拼音：{}'.format(en.strip('、')))
    print('符号：{}'.format(symbol.strip('、')))
# split_str('我的名字是lemon,今年5岁。')
