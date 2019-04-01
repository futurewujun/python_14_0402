# -*- coding: utf-8 -*-
import pandas
res = pandas.read_excel('py14.xlsx')
# print(res.values)
print(res.ix[0].values)