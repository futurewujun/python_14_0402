# -*- coding: utf-8 -*-
# 6:利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：
# # 冒泡排序：小的排前面，大的排后面。   --- 依次比较两个相邻的元素，如果他们的顺序（按大小）错误就把他们交换过来
# a=[1,7,4,89,34,2]
问题。
a=[1,7,4,89,34,2,3,2,32,332,32341,2341234,1,4234]      # 有重复数字时不正确
for i in range(len(a)-1):        # 循环的次数
    for j in range(len(a)-1):    # 遍历排序
        if a[j]>a[j+1]:   # 若前面值大于后面
            m = a[j]    # m 为中间桥梁,先将前面值存在m中
            a[j]=a[j+1]   # 将后面值赋予前面  值
            a[j+1]=m      # 将m，即前面值赋予后面值
print(a)

# a = [1, 7, 4, 89, 34, 2]
a=[1,7,4,89,34,2,3,2,32,332,32341,2341234,1,4234]    # 有重复数字时不正确
print('原列表为{}'.format(a))
for i in range(6):
    for j in range(i + 1, 6):
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
print('冒泡排序后的列表为{}'.format(a))
# 标准
a=[1,7,4,89,34,2,3,2,32,332,32341,2341234,1,4234]
for i in range(len(a)-1) :    # 循环的次数
    for j in range(len(a)-1):    # 开始比较
        if a[j]<a[j+1]:
            pass
        else:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
# 取随机数，然后排序
import  random
a=[random.randint(1,100)for i in range(10) ]
print(a)
for i in range(len(a)-1) :
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)