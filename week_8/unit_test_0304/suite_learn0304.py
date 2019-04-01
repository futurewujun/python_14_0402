# -*- coding: utf-8 -*-
import unittest
from week_8.unit_test_0304.unit_test_learn0304 import *   #具体到类
from week_8.unit_test_0304 import unit_test_learn0304   #具体到模块
import HTMLTestRunnerNew    #测试报告
suite=unittest.TestSuite()  #测试套件
#添加用例
# # 方法一：
suite.addTest(TestAdd('test_001'))    #添加测试用例的实例，可只添加指定的用例
# suite.addTest(TestAdd('test_002'))

# Loader专门来加载用例  --- 两种方式
# 方法二： 通过测试类进行添加
# loader=unittest.TestLoader() #加载用例
# suite.addTest(loader.loadTestsFromTestCase(TestAdd)) #直接传入类名

# 方法三：通过测试模块进行添加 ---导入时需要只导入模块
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(unit_test_learn0304))


#执行用例
# with open('test.txt_02','w',encoding='utf-8') as file:
    # runner=unittest.TextTestRunner( stream=file, descriptions=True, verbosity=2)    #实例化,2最详细
with open('test0304.html','wb') as file:   #写到html中新建要以wb方式，且不需要写encoding编码，文件为html格式
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='20190304测试报告_py14',
                                            description='2019第一次报告',tester='未来')
    runner.run(suite)   #执行测试套件里的用例








