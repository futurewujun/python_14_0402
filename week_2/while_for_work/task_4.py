# -*- coding: utf-8 -*-
# # 4：请用嵌套for循环输出如下等边三角形（三个边均为5个*）   #
#        *
#      *  *
#    *  *   *
#   *  *  *  *
# *   *  *  *  *
#
# for a in range(1,6):
#     print(' '*(5-a),end='')
#     for b in range(1,a+1):
#         print('* '*a)
#         break   # 循环执行一次就break
# #
# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print(' ',end='')
#     for k in range(i):
#         print('*',end=' ')
#     print('')
#
# for a in range(1,6):
#     print(' '*(5-a),end='')   # 一个循环后 不换行输出下面的值
#     print('* '*a)

# 先输出左边的空格（里面的for循环）
for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    print('* '*i)
