# -*- coding: utf-8 -*-
# 求0-100的和
# sum = 0
# for i in range(0,101):
#     sum+=i
# print(sum)

# sum=0
# i=0
# while 1:
#     i+=1
#     sum+=i
#     if i == 100:
#         print(sum)
#         break

# 打印直角三角形：
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     print('*'*i)
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
# 打印等边三角形：
#        *
#      *  *
#    *  *   *
#   *  *  *  *
# *   *  *  *  *
a=[1,2,3]
print(len(a))
b='@#$@'
print(b.join('we'))
b.split()
print(b.replace('@','1',))
# del a
# print(a)
print(a.pop(1))
print(a)
m={'name':'python','age':'14'}
print(m.copy())
print(m)
print(m.fromkeys('qwe','123'))
print(list(m.items()))
print(m.keys())
print('age' in m)