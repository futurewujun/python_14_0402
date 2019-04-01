# -*- coding: utf-8 -*-
import unittest
class TestAdd(unittest.TestCase):   #继承
    '''加法'''
    def setUp(self):    #拓展，重写---开始，准备工作，测试环境
        print('---开始执行用例---')
    def tearDown(self): #拓展，重写---结束，清场工作，环境
        print('---用例执行完毕---')
    #用例以test开头
    def test_001(self,a,b,expect): #两个整数相加
        # a=1
        # b=2
        # expect=4
        c=a+b
        try:
            self.assertEqual(c,expect)  #断言
        except AssertionError as e:
            print('001用例执行失败，错误是{}'.format(e))
            raise e #抓取异常之后要抛出异常
        print('测试结果是：{}'.format(c))
    def test_002(self): #两个负数相加
        a = -1
        b = -2
        expect=-2
        c = a+b
        print('测试结果是：{}'.format(c))
    def test_003(self): #一正一负相加
        a = -1
        b = 2
        expect=2
        c = a + b
        print('测试结果是：{}'.format(c))

