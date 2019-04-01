# -*- coding: utf-8 -*-
# 1：引入单元测试
# 2：引入ddt
# 3：测试用例里面引入引入try...except..finally，并写回测试结果
# 4：引入日志
# 5：完成用例的可配置化：想跑哪条用例，就在配置文件里面写好
# 6：搞定全局变量（path变量，数据与文件分离）

# 投资 增加数据库的校验，可以写断言也可以写会数据库检查的结果到Excel
import unittest
from ddt import ddt,data
from API_Program.API_05.common.do_excel import DoExcel
from API_Program.API_05.common.log_test import MyLog
from API_Program.API_05.common.http_request import HttpRequest
from API_Program.API_05.common import project_path
from API_Program.API_05.common.get_data import GetData
from API_Program.API_05.common.do_sql import DoSql
# 测试数据
addloan_data=DoExcel(project_path.case_path,'Addloan').read_data('AddloanCase')
# print(addloan_data)

@ddt
class RunCase(unittest.TestCase):
    def setUp(self):
        '''准备测试数据，测试前的准备工作'''
        self.do_exl=DoExcel(project_path.case_path,'Addloan')
        self.my_log=MyLog()
        self.http=HttpRequest()
    @data(*addloan_data)
    def test_case(self,case):
        global result
        # 取到request里需要的参数
        url=case['Url']
        method=case['Method']
        expected=eval(case['ExpectedResult'])   #转换为原本的类型
        param=eval(case['Params'])

        if case['Params'].find('normal_phone') != -1:
            param['mobilephone']=getattr(GetData,'normal_phone')

        # 判断是否要执行sql语句，存在sql就执行
        if case['Sql'] != None:
            sql=eval(case['Sql'])['sql']
            # print(eval(case['Sql']))
            # print(type(eval(case['Sql'])))
            loan_id=DoSql().do_sql(sql,1)[0]
            setattr(GetData,'LOANID',loan_id)#将新的loanid赋值给loan_id
        # 进行审核到4状态，替换loan_id  #请求之前替换
        if 'loan_id' in case['Params']:
        # if case['Params'].find('loan_id') != -1:
        #     param=eval(case['Params'].replace('loan_id',str(getattr(GetData,'LOANID'))))  #replace 只能对字符串进行操作，要str强转
            param['id']=getattr(GetData,'LOANID')
        # else:
        #     param=eval(case['Params'])
        # print(param)
        # # 拿到本次竞标前标的剩余金额：
        # if case['Sql'] != None:
        #     before_LeaveAmount=DoSql().do_sql(eval(case['Sql'])['sql_2'],1)[0]
        #     print(before_LeaveAmount)

        # 准备测试
        self.my_log.info('开始执行{}模块第{}条用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        self.my_log.info('参数是:{}'.format(param))

        res=self.http.http_request(method,url,param,cookies=getattr(GetData,'cookies'))
        print('实际结果是：{}'.format(res.json()))

        # 判断是否有cookies,有就将cookies重新根据反射赋值
        if res.cookies:
            setattr(GetData,'cookies',res.cookies)
        try:
            self.assertEqual(expected['code'],res.json()['code'])
            # 拿到投资后的剩余金额：
            # if case['Sql']!=None:
            #     sql=eval(case['Sql'])['sql_2']
            #     after_LeaveAmount=DoSql().do_sql(sql,1)[0]
            #
            #     invest_amount = param['amount']
            #     expected_amount=after_LeaveAmount - invest_amount
            #     self.assertEqual(expected_amount,after_LeaveAmount)

            result='pass'
            self.my_log.info('该条测试用例通过')
        except AssertionError as e:
            result='failed'
            self.my_log.error('该条用例不通过：{}'.format(e))
            # raise e
        finally:
            final_result=result
            self.my_log.info('******开始写入数据******')
            self.do_exl.write_back(case['CaseId']+1,9,res.text) #写入实际结果
            self.do_exl.write_back(case['CaseId']+1,10,final_result)   #写入测试结果
            self.my_log.info('******写入数据完毕******')
