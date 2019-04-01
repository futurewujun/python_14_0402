# -*- coding: utf-8 -*-
#3）新建一个run.py文件， 在这里面完成Excel数据的读取以及完成用例的执行，并写回测试结果到Excel文档里面。 至此已经完成了接口自动化测试的第一步。
from week_8.task_0308.request_excel import HttpRequest,DoExcel
import unittest
from ddt import ddt,data,unpack
import json
test_data=DoExcel().read_excel()    #测试数据
# print(test_data)

@ddt    #修饰测试类,所以必须结合unittest来使用
class RunCase(unittest.TestCase):
    def setUp(self):
        print('------开始执行用例：')
    def tearDown(self):
        print('------用例执行完毕：')
    # 写用例   --- 以test开头
    @data(test_data)#装饰测试用例，
    def test_01(self,a):
        # 执行http请求
        url=a[0][2]
        param=eval(a[0][5])
        method='get'
        ac=HttpRequest(url,param,method).http_request()
        wte_exl=DoExcel()
        wte_exl.write_result(row=2, column=8, value=ac)  # 写实际结果
        act=json.loads(ac)
        expected=eval(a[0][6])
        print('实际结果是：{}'.format(act))
        print('期望结果是：{}'.format(expected))
        try:
            self.assertEqual(act['code'],expected['code'])
            wte_exl.write_result(row=2,column=9,value='pass')  #写测试结果
            print('测试通过')
        except AssertionError as  e:
            print('断言错误：{}'.format(e))
            wte_exl.write_result(row=2, column=9, value='failed')
            print('测试不通过')
            raise e
    @data(test_data)  # 装饰测试用例，
    def test_02(self,a):
        # 执行http请求
        url=a[1][2]
        param=eval(a[1][5])
        method = 'get'
        ac = HttpRequest(url, param, method).http_request()
        wte_exl = DoExcel()
        wte_exl.write_result(row=3, column=8, value=ac)  # 写实际结果
        act=json.loads(ac)
        expected=eval(a[1][6])  #
        print('实际结果是：{}'.format(act))
        print('期望结果是：{}'.format(expected))
        try:
            self.assertEqual(act['code'],expected['code'])
            wte_exl.write_result(row=3,column=9,value='pass')   #写测试结果
            print('测试通过')
        except AssertionError as  e:
            print('断言错误：{}'.format(e))
            wte_exl.write_result(row=3, column=9, value='failed')
            print('测试不通过')
            raise e

    @data(test_data)  # 装饰测试用例，
    def test_03(self, a):
        # 执行http请求
        url = a[2][2]
        param = eval(a[2][5])
        method = 'get'
        ac = HttpRequest(url, param, method).http_request()
        wte_exl = DoExcel()
        wte_exl.write_result(row=4, column=8, value=ac)  # 写实际结果
        act = json.loads(ac)
        expected = eval(a[2][6])  #
        print('实际结果是：{}'.format(act))
        print('期望结果是：{}'.format(expected))
        try:
            self.assertEqual(act['code'], expected['code'])
            wte_exl.write_result(row=4, column=9, value='pass')  # 写测试结果
            print('测试通过')
        except AssertionError as  e:
            print('断言错误：{}'.format(e))
            wte_exl.write_result(row=4, column=9, value='failed')
            print('测试不通过')
            raise e

    @data(test_data)  # 装饰测试用例，
    def test_04(self, a):
        # 执行http请求
        url = a[3][2]
        param = eval(a[3][5])
        method = 'get'
        ac = HttpRequest(url, param, method).http_request()
        wte_exl = DoExcel()
        wte_exl.write_result(row=5, column=8, value=ac)  # 写实际结果
        act = json.loads(ac)
        expected = eval(a[3][6])  #
        print('实际结果是：{}'.format(act))
        print('期望结果是：{}'.format(expected))
        try:
            self.assertEqual(act['code'], expected['code'])
            wte_exl.write_result(row=5, column=9, value='pass')  # 写测试结果
            print('测试通过')
        except AssertionError as  e:
            print('断言错误：{}'.format(e))
            wte_exl.write_result(row=5, column=9, value='failed')
            print('测试不通过')
            raise e

    @data(test_data)  # 装饰测试用例，
    def test_05(self, a):
        # 执行http请求
        url = a[4][2]
        param = eval(a[4][5])
        method = 'get'
        ac = HttpRequest(url, param, method).http_request()
        wte_exl = DoExcel()
        wte_exl.write_result(row=6, column=8, value=ac)  # 写实际结果
        act = json.loads(ac)
        expected = eval(a[4][6])  #
        print('实际结果是：{}'.format(act))
        print('期望结果是：{}'.format(expected))
        try:
            self.assertEqual(act['code'], expected['code'])
            wte_exl.write_result(row=6, column=9, value='pass')  # 写测试结果
            print('测试通过')
        except AssertionError as  e:
            print('断言错误：{}'.format(e))
            wte_exl.write_result(row=6, column=9, value='failed')
            print('测试不通过')
            raise e

    @data(test_data)  # 装饰测试用例，
    def test_06(self, a):
        # 执行http请求
        url = a[5][2]
        param = eval(a[5][5])
        method = 'get'
        ac = HttpRequest(url, param, method).http_request()
        wte_exl = DoExcel()
        wte_exl.write_result(row=7, column=8, value=ac)  # 写实际结果
        act = json.loads(ac)
        expected = eval(a[5][6])  #
        print('实际结果是：{}'.format(act))
        print('期望结果是：{}'.format(expected))
        try:
            self.assertEqual(act['code'], expected['code'])
            wte_exl.write_result(row=7, column=9, value='pass')  # 写测试结果
            print('测试通过')
        except AssertionError as  e:
            print('断言错误：{}'.format(e))
            wte_exl.write_result(row=7, column=9, value='failed')
            print('测试不通过')
            raise e



