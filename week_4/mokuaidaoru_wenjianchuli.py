# -*- coding: utf-8 -*-

f=open('py1.txt')    # 打开文件
f2=open('../qwe')
f1=open('E:\PycharmProjects\python_14\week_3\py14.txt')
# open('../../week_3/py14.txt')
# E:\PycharmProjects\python_14\week_3\py14.txt
# print(f1.read())
# print(f2.read())
# print(f.read())

# os 可以完成对文件的读取
import os
path=os.getcwd()       # 获取当前的工作目录
path1=os.path.realpath(__file__)  # (__file__)表示当前文件。---获取文件所在的路径。绝对路径
path2=os.path.basename(__file__)  # 获取当前文件名
path_1=os.path.relpath(__file__)
path_2=os.path.relpath(path)
print(path)
print(path1)
print(path2)
print(path_1)
# 切割路径：
path3=os.path.realpath(__file__)
path4=os.path.split(path3)  # 返回文件夹路径与文件名为元素的元组
print(path4)        # ('E:\\PycharmProjects\\python_14\\week_4', 'mokuaidaoru_wenjianchuli.py')
path5=os.path.split(os.path.split(path3)[0])    # 对取到的文件夹路径再次切割，可以多次切割，拿到想要的路径或者文件名
print(path5)        # ('E:\\PycharmProjects\\python_14', 'week_4')

# 路径的拼接
path6=os.path.split(os.path.realpath(__file__))[0]
path7=os.path.join(path6,'py1.txt')     # 前面是原路径，后面是需要拼接上的路径
print(path7)
print(open(path7,encoding='utf-8').read())  # 拼接路径后，可以拿到新路径直接读写，省去了取绝对路径的麻烦