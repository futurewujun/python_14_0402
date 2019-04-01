# -*- coding: utf-8 -*-
# 3）新建一个run.py文件， 在这里面完成Excel数据的读取以及完成用例的执行，并写回测试结果到Excel文档里面。 至此已经完成了接口自动化测试的第一步。

from API_Program.Task.API_01.common.write_cases1 import RunCase
import unittest
import HTMLTestRunnerNew
class RunTest:

    def run_test(self):
        suite=unittest.TestSuite()  #测试套件
        loader=unittest.TestLoader()    #加载用例
        suite.addTest(loader.loadTestsFromTestCase(RunCase))
        # 执行用例
        with open('ApiTestReport_01.html','wb') as file:
            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                    verbosity=2,
                                                    title='前程贷接口测试报告',
                                                    description='注册接口测试报告',
                                                    tester='未来')
            runner.run(suite)
a=RunTest()
a.run_test()
