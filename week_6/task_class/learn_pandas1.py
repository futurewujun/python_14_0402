# -*- coding: utf-8 -*-
import pandas as pd
# 默认把第一行作为表头
df=pd.read_excel('py_14.xlsx')
print(df.values)
# 要读第一行，要把作为的表头加上数据
# 读取第一行的数据
print(df.ix[0].values)
# 读取指定行，指定列
print(df.ix[2,1].values)