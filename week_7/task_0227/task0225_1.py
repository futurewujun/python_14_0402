# -*- coding: utf-8 -*-
#写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串
import configparser
cf = configparser.ConfigParser()    #创建对象
class ReadData:
    '''#1：读取整数；2：读取浮点数；3：读取布尔值；4：读取其他类型的数据 list tuple dict eval（）；5：读取字符串'''
    def __init__(self,file_name):
        self.file_name = file_name
    def read_int(self,section,option):
        cf.read(self.file_name,encoding='utf-8')    #打开配置文件
        res = cf.getint(section,option)    #读取信息
        return res
    def read_float(self,section,option):
        cf.read(self.file_name,encoding='utf-8')
        res = cf.getfloat(section,option)
        return res
    def read_boolean(self,section,option):
        cf.read(self.file_name,encoding='utf-8')
        res = cf.getboolean(section,option)
        return res
    def read_else_date(self,section,option):
        '''读取其他类型数据'''
        cf.read(self.file_name,encoding='utf-8')
        res = cf.get(section,option)
        return eval(res)    #变为本身的类型
    def read_str(self,section,option):
        cf.read(self.file_name,encoding='utf-8')
        res = cf.get(section,option)   #直接get就是返回字符串类型
        # res = cf['StrData']['str']  #取值的另一种方式
        return res
if __name__ == '__main__':
    exam=ReadData('data_1.conf')
    print(exam.read_str('StrData','logger_name'))