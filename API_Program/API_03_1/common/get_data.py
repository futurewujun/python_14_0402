# -*- coding: utf-8 -*-

class GetData:
    '''动态的更改、删除、获取 数据'''
    cookies=None    #属性

if __name__ == '__main__':

    print(GetData.cookies)  # 类名直接调用属性取值
    print(GetData().cookies)    #实例化调用属性 取值

    # 利用反射的机制 取值
    # 第一个参数是类名，第二个参数是属性的参数名
    print(getattr(GetData,'cookies'))   #取值
    print(setattr(GetData,'cookies','lemon'))   #重新赋值
    print(hasattr(GetData,'cookies'))   #判断是否有属性值
    print(getattr(GetData,'cookies'))
    print(delattr(GetData,'cookies'))   #删除属性