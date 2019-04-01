# -*- coding: utf-8 -*-
import configparser
class ReadConfig:
    cf=configparser.ConfigParser()  #创建对象
    cf.read('data_1.conf',encoding='utf-8') #打开配置文件
