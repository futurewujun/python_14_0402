# -*- coding: utf-8 -*-
# 1：引入单元测试
# 2：引入ddt
# 3：测试用例里面引入引入try...except..finally，并写回测试结果
# 4：引入日志
# 5：完成用例的可配置化：想跑哪条用例，就在配置文件里面写好
# 6：搞定全局变量（path变量，数据与文件分离）
import unittest
from ddt import ddt,data
from API_Program.API_03_1.common.do_excel import DoExcel
from API_Program.API_03_1.common.log_test import MyLog
from API_Program.API_03_1.common.http_request import HttpRequest
from API_Program.API_03_1.common import project_path
from API_Program.API_03_1.common.get_data import GetData
# 测试数据
bidloan_data=DoExcel(project_path.case_path,'Bidloan').read_data('BidloanCase')

@ddt
class RunCase(unittest.TestCase):
    def setUp(self):
        '''准备测试数据，测试前的准备工作'''
        self.do_exl=DoExcel(project_path.case_path,'Bidloan')
        self.my_log=MyLog()
        self.http=HttpRequest()
    @data(*bidloan_data)
    def test_case(self,case):
        global result
        # 取到request里需要的参数
        url=case['Url']
        param=eval(case['Params'])
        method=case['Method']
        expected=eval(case['ExpectedResult'])
        # 准备测试
        self.my_log.info('开始执行{}模块第{}用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        self.my_log.info('参数是:{}'.format(param))

        res=self.http.http_request(method,url,param,cookies=getattr(GetData,'cookies'))
        print('实际结果是：{}'.format(res.json()))
        # 判断是否有cookies,有就将cookies重新根据反射赋值
        if res.cookies:
            setattr(GetData,'cookies',res.cookies)
        try:
            self.assertEqual(expected['code'],res.json()['code'])
            result='pass'
            self.my_log.info('该条测试用例通过')
        except AssertionError as e:
            result='failed'
            self.my_log.error('该条用例不通过：{}'.format(e))
        finally:
            final_result=result
            self.my_log.info('******开始写入数据******')
            self.do_exl.write_back(case['CaseId']+1,8,res.text) #写入实际结果
            self.do_exl.write_back(case['CaseId']+1,9,final_result)   #写入测试结果
            self.my_log.info('******写入数据完毕******')
