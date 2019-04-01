# -*- coding: utf-8 -*-
# 1：编写一个日志类，能够实现输出文件到指定文件和console
# 2：结合配置文件类实现日志类的可配置，具体参考老师的代码以及视频
# 3：结合日志类以及do_excel类，加上异常判断 与日志输出
import logging
from week_7.task_0227.task0225_1 import ReadData
from week_7.task_0227.task_0222_1 import DoExcel
class MyLog:
    def __init__(self):
        self.logger_name=ReadData('data_1.conf').read_str('StrData','logger_name')

    def my_log(self,level,msg):
        my_logger=logging.getLogger(self.logger_name) #定义一个日志收集器，并且命名
        my_logger.setLevel('DEBUG') #设置收集器级别 ------- 收集器级别？--------------------------------------------------
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-[%(name)s]-[日志信息]:%(message)s') #设置日志格式
        sh=logging.StreamHandler()  #设置输出到控制台
        sh.setLevel('DEBUG')    #设置级别
        sh.setFormatter(formatter)  #设置格式
        fh=logging.FileHandler('my_test.log',encoding='utf-8')  #设置输出到文本
        fh.setLevel('DEBUG')    #设置级别
        fh.setFormatter(formatter)  #设置格式
        #将设置的输出方式添加到设置的收集器，对接-取两者交集
        my_logger.addHandler(sh)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        # 移除
        my_logger.removeHandler(fh)
        my_logger.removeHandler(sh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)    #调用my_log函数
    def info(self,msg):
        self.my_log('INFO',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

    def read_case(self,button):
        self.info('开始读取数据')
        try:
            DoExcel().read_date('test_case.xlsx', 'Sheet1', button)
            self.info('数据读取完毕')
        except Exception as e:
            # print('数据读取失败，错误是:{}'.format(e))
            self.error(e)
            self.info('数据读取失败')

if __name__ == '__main__':
    button=ReadData('case_1.conf').read_str('CASE','button')
    exc_logger=MyLog()
    # exc_logger.info('提示信息')
    exc_logger.read_case(button)




