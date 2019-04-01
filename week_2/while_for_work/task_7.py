# -*- coding: utf-8 -*-
# 7:有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？
s = 0
list = [1,2,3,4]
for a in list:
    for b in list:
        for c in list:
            if a != b and a != c and b != c:
                # print(a,b,c)
                print(str(a)+str(b)+str(c)+',',end='')
                s += 1
    print()
print(s)

count = 0
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            for k in range(1, 5):
                if i != k and j != k:
                    num = str(i) + str(j) + str(k)
                    count += 1
                    print(num, end='、')
    print()
print('所以：1,2,3,4能组成一共 {} 个互不相同且无重复数字的三位数'.format(count))

import os
print(os.path.realpath(__file__))