# -*- coding: utf-8 -*-
class TestEngineer:  # 驼峰命名
    # 属性
    salary = 200000
    week_time = 3
    # 行为
    def do_api_testing(self):   # 对象方法， 这个方法只能对象来调用。 self：类本身
        print('self的值：',self)
        print("会接口测试")
    def do_sql(self):
        print("会操作数据库")
    @classmethod                # 引入类方法
    def do_function_testing(cls):
        print("会功能测试")
    @staticmethod               # 引入静态方法，此时就可以不传参数 self。 不是对象也可以调用下面的方法
    def coding(self):      #  就直接将self变为了一个参数,也可以不传参数
        print('会写代码：',self)
p1=TestEngineer() # p1 是对象
p2=TestEngineer()
print(p1.salary)
p1.do_api_testing()      # p1 调用方法
print('p1的值：',p1)       # 内存地址一样，即self就是对象本身，调用类的方法即对象方法必须只能是对象来调用，不能用类或者其他的调用
p2.do_function_testing()    # p2调用方法
p3=TestEngineer    # p3不是对象，只是个变量
p3.coding('python')  # 此方法，定义了静态方法，所以变量也可以调用这个方法---
TestEngineer.coding('java')

