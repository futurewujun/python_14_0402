# -*-coding:utf-8-*-
# @Time      :2019/2/27/027 20:25
# @Author    :Tanxi
# @Email     :1410510771@qq.com
# @File      :read_config.py
# @Software  :PyCharm Community Edition

#写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串

from configparser import ConfigParser

class ReadConfig:
    '''读取配置文件'''
    def __init__(self,filename):
        '''
        :param filename: 需要读取的配置文件名
        '''
        self.cf=ConfigParser()
        self.cf.read(filename,encoding='utf-8')

    def read_int(self,section,option):
        '''读取整形数据'''
        value=self.cf.getint(section,option)
        return value

    def read_float(self,section,option):
        '''读取浮点型数据'''
        value=self.cf.getfloat(section,option)
        return value

    def read_bool(self,section,option):
        '''读取布尔值类型数据'''
        value=self.cf.getboolean(section,option)
        return value

    def read_itera(self,section,option):
        '''读取列表、元组、字典类型数据'''
        value=self.cf.get(section,option)
        return eval(value)

    def read_str(self,section,option):
        '''读取字符串类型数据'''
        value=self.cf.get(section,option)
        return value

# if __name__ == '__main__':
#     t=ReadConfig('config.conf')
#     print(t.read_int('host','port'))
#     print(t.read_float('option', 'ddd'))
#     print(t.read_bool('option', 'fff'))
#     print(t.read_itera('option', 'aaa'))
#     print(t.read_itera('option', 'bbb'))
#     print(t.read_itera('option', 'ccc'))
#     print(t.read_str('host', 'host'))
#     print(t.read_str('mysql', 'db_name'))