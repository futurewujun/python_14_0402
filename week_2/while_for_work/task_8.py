# -*- coding: utf-8 -*-
# 8:求 0—7 所能组成的奇数个数
# 最小值为0，最大值为7777777
问题？
s = 1
count = 0   # 存奇数个数
for i in range(1,9):      # 位数为8
    if i == 1:            # 一位数时
        s = 4
    elif i == 2:          # 二位数时
        s = 4*7
    else:
        s = s*8
    count += s
print(count)

# 分析：个位时奇数即为奇数，0-7中1，3，5，7为奇数，；利用数学排列组合得出以下：
# 一位数奇数个数：4
# 两位数奇数个数：7*4
# 三位数奇数个数：7*8*4
# 四位数奇数个数：7*8*8*4
# ............
# 八位数奇数个数：7*8*8*8*8*8*8*4
count = 1
sum = 0
for i in range(1, 9):
    if i == 1:
        count = 4
    elif i == 2:
        count = 4 * 7
    else:
        count *= 8
    sum += count
    print('{}位数时，奇数个数为{}'.format(i, count))
print('综上：0-7一共能组成 {} 个奇数'.format(sum))

s = 1
sum_=0
for i in range(1,9):
    if i ==1:
        s = 4
    elif i ==2:
        s =4*7
    if i>2:
        s *=8
    sum_ +=s
    print('%d位数的奇数个数为%d'%(i,s))
print('总和为：sum=%d'%sum_)