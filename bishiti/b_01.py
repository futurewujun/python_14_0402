# -*- coding: utf-8 -*-
#从字符串’abcdba‘中找出第一个不重复的字符，方法不限
# m='abcdqwebdcaqwel'
# n=[]
# for i in range(0,len(m)):
#     if m[i] not in n:
#         n.append(m[i])
#     else:
#         n.remove(m[i])
#
# print(n)
# print(n[0])
#
# #
import unittest
from ddt import ddt,data,unpack

@ddt #装饰测试类
class TestPringMsg(unittest.TestCase):
    @data(1,2,4,5,9)#装饰测试用例([1,2,3],(4,5,9))
    def test_001(self,a):#如果用了unpack 必须用对应个数的参数名来进行接收

        print('a:',a)
