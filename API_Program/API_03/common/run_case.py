# -*- coding: utf-8 -*-
# 1：引入单元测试
# 2：引入ddt
# 3：测试用例里面引入引入try...except..finally，并写回测试结果
# 4：引入日志
# 5：完成用例的可配置化：想跑哪条用例，就在配置文件里面写好
# 6：搞定全局变量（path变量，数据与文件分离）
import unittest
from ddt import ddt,data
import json
from API_Program.API_03.common.do_excel import DoExcel
from API_Program.API_03.common.http_request import HttpRequest
from API_Program.API_03.common import project_path
from API_Program.API_03.common.log_test import MyLog

#读取到测试数据
# 注册登录：
Register_Login=DoExcel(project_path.case_path).read_data('Register_Login')
# 充值提现
Recharge_Withdraw=DoExcel(project_path.case_path).read_data('Recharge_Withdraw')


@ddt    #修饰测试类
class RunCase(unittest.TestCase):
    def setUp(self):
        self.do_exl=DoExcel(project_path.case_path)    # 准备测试数据
        self.my_log=MyLog()
    # 登录注册
    @data(*Register_Login)   # 加*解包，相当于遍历test_data传入函数，与加unpack的区别是：加入了unpack后，date里有几个参数，下面的函数就要传入几个变量
    def test_case(self,case):
        global result   #声明全局变量
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])
        # print(param)

        expected=eval(case['ExpectedResult'])
        #发起测试
        # print('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        self.my_log.info('正在执行{}模块第{}条用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        self.my_log.info('参数是：{}'.format(param))
        res=HttpRequest()  #实例化
        resp=res.http_request(method,url,param,cookies=None)
        print('实际结果：{}'.format(resp.json()))#http发送请求拿到的实际返回值
        #对比结果
        try:
            self.assertEqual(expected,resp.json())
            result='pass'
            self.my_log.info('该条测试用例通过')
            # print('该条测试用例通过')
        except  AssertionError as e:
            result='failed'
            self.my_log.error('该条测试用例不通过：'.format(e))
            # print('该条测试用例不通过:{}'.format(e))
        finally:
            final_result=result
            self.my_log.info('******开始写入数据******')
            self.do_exl.write_back('Register_Login',case['CaseId']+1,8,resp.text)   #写实际结果   #03：不同的表单写回，表单名就不能放在初始化函数中
            self.do_exl.write_back('Register_Login',case['CaseId']+1,9,final_result)    #写测试结果
            self.my_log.info('******写入数据完毕******')

    # 充值提现
    @data(*Recharge_Withdraw)
    def test_case2(self,case_2):
        global result1
        url_login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        param_login={'mobilephone':'18688775656','pwd':'123456'}
        method_login='get'
        # 获取到登录的cookies
        cookies=HttpRequest().http_request(method_login,url_login,param_login,cookies=None).cookies
        url=case_2['Url']
        param=eval(case_2['Params'])
        method=case_2['Method']
        expected=eval(case_2['ExpectedResult'])
        self.my_log.info('正在执行{}模块第{}条用例：{}'.format(case_2['Module'],case_2['CaseId'],case_2['Title']))
        self.my_log.info('参数是：{}'.format(param))
        res=HttpRequest()   #实例化
        resp=res.http_request(method,url,param,cookies=cookies) #带入登录的cookies
        print('实际结果是：{}'.format(resp.json()))   #发起请求的实际结果
        # 对比结果
        try:
            self.assertEqual(expected['code'],resp.json()['code'])  #对比code
            result1='pass'
            self.my_log.info('该条测试用例通过')
        except AssertionError as e:
            self.my_log.error('该条测试用例不通过：{}'.format(e))
            result1='failed'
        finally:
            final_result=result1
            self.my_log.info('******开始写入数据******')
            self.do_exl.write_back('Recharge_Withdraw',case_2['CaseId']+1,8,resp.text)
            self.do_exl.write_back('Recharge_Withdraw',case_2['CaseId']+1,9,final_result)
            self.my_log.info('******写入数据完毕******')





