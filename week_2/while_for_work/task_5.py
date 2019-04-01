# -*- coding: utf-8 -*-
# 5:输出99乘法表    ---  嵌套for循环
for a in range(1,10):
    for b in range(1,a+1):
        print('{}*{}={} '.format(b,a,a*b),end='')   # end=''，不换行输出，
    print()     # 每个for循环完成后就换行b（不是每次循环完就换行）

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}'.format(j, i, i * j), end='\t')
    print('')
