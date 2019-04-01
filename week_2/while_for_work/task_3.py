# -*- coding: utf-8 -*-
# 3：利用for循环输出如下三角形:
# *
# **
# ***
# ****
# *****
for i in range(1,6):      # i 取1-5
    print(i*'*')
# 第一行一个，第二行二个，第三行三个...
for i in range(5):
    for j in range(i + 1):
        print("*", end='')
    print()




