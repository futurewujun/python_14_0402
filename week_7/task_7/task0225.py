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
        cf.read(self.file_name, encoding='utf-8')  # 打开配置文件
    def read_int(self):

        res = cf.getint('IntegerData','int')    #读取信息
        return res
    def read_float(self):

        res = cf.getfloat('FloatData','flo')
        return res
    def read_boolean(self):

        res = cf.getboolean('BooleanData','bol')
        return res
    def read_else_date(self):
        '''读取其他类型数据'''

        res = cf.get('ElseData','els1')
        return res
    def read_str(self):

        res = cf.get('StrData','str')   #直接get就是返回字符串类型
        # res = cf['StrData']['str']  #取值的另一种方式
        return res
if __name__ == '__main__':
    exam=ReadData('data_1.conf')
    print(exam.read_int(),',','类型是：',type(exam.read_int()))
    print(exam.read_float(),',','类型是：',type(exam.read_float()))
    print(exam.read_boolean(),',','类型是：',type(exam.read_boolean()))
    print(exam.read_else_date(),',类型是：',type(eval(exam.read_else_date())))
    print(exam.read_str(),',','类型是：',type(exam.read_str()))