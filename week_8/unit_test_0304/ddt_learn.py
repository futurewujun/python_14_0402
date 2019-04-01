# -*- coding: utf-8 -*-
# ddt   --- date drive test
# 数据驱动测试
# 安装：pip install ddt

import unittest
from ddt import ddt,data,unpack

test_data=[[1,2,3],[3,-2,1]]
test_data_dic=[{'a':1,'b':2,'expected':3}]
# @ddt    #装饰测试类，所以必须结合unittest来使用
# class TestPrintMsg(unittest.TestCase):  #继承，并不是实例化
#
#     @data((1,2,3),[4,5,9])    #装饰测试用例，把数据传进来组成一个元组，再对元组进行遍历
#     @unpack #对data传递过来的元组的子元素进行拆分，要求是 可迭代的，元组有几个子元素，下面的用例函数就要传几个参数；前后元素参数不一致就传默认参数或者传为None
#     def test_001(self,a,b,expected):
#         c=a+b
#         self.assertEqual(c,expected)
#
#         print('a:',a)
#         # c=a+b
#         # self.assertEqual(c,expect)
@ddt
class TestAdd(unittest.TestCase):
    @data(*test_data)   #[[1,2,3],[3,-2,1]] --->  ([[1,2,3],[3,-2,1]],)  所以加* 先去一层
    @unpack
    def test_02(self,a,b,expected):
        c=a+b
        self.assertEqual(c,expected)
''' ------ 必须要鼠标在最后面，然后再右键运行程序----'''