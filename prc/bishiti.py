# -*- coding: utf-8 -*-
a=[1,[[2],3,4],5]
b=[]
for i in a:
    print(i)
    b.append(a[0])

    b.append(a[1][0][0])
    b.append(a[1][1])
    b.append(a[1][2])
    b.append(a[2])
print(b)
# c=list(set(b))  # 去重
c=sorted(set(b),key=b.index)    # 去重且保持原有顺序
# 遍历完成
d=[]
for j in b:
    if j not in d:
        d.append(j)
print(d)

print(c)
