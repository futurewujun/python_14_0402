# -*- coding: utf-8 -*-
import re
from API_Program.API_06.common.get_data import GetData
p = '#(.*?)#'
target="{'mobilephone':'#normal_phone#','pwd':'#normal_pwd#'}"
while re.search(p,target):  #找到参数化的字符就返回一个 match object, 即True

    m=re.search(p,target)   #在字符串里根据正则表达式来查找，有匹配的就返回match object
    key=m.group(1)  #拿到key，填参数1是只取 需要的字符串，不包括符号
    value=getattr(GetData,key)    #取到要替换的内容
    target=re.sub(p,value,target,count=1)  #替换一次,赋值给新的字符串
print(target)


