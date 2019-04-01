# -*- coding: utf-8 -*-
# 配置类
import configparser
cf=configparser.ConfigParser()  #创建对象
class ReadConf:
    def __init__(self,file_name):
        self.file_name=file_name
    def read_button(self):
        cf.read(self.file_name,encoding='utf-8')    #打开配置文件

