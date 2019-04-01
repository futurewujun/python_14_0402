# -*- coding: utf-8 -*-
import unittest
from week_7.unit_test_0301.unit_test_learn import *
suite=unittest.TestSuite()  #测试套件
#添加用例
suite.addTest(TestAdd('test_001'))    #添加测试用例的实例
suite.addTest(TestAdd('test_002'))
#执行用例
with open('test.txt','w',encoding='utf-8') as file:
    runner=unittest.TextTestRunner( stream=file, descriptions=True, verbosity=2)    #实例化,2最详细
    runner.run(suite)   #执行测试套件里的用例
