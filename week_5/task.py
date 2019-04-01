# -*- coding: utf-8 -*-
# 1：编写一个数学类，要求初始化函数带a,b,c,d4个参数，然后有加减乘除四个函数
class Math:
    '''数学类，运算 加减乘除'''
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def add(self):
        s=self.a+self.b+self.c+self.d
        print('加法：',s)
    def subtraction(self):
        sub=self.a-self.b-self.c-self.d
        print('减法：',sub)
    def multiplication(self):
        mul=self.a*self.b*self.c*self.d
        print('乘法：',mul)
    def division(self):
        div=self.a/self.b/self.c/self.d
        print('除法：',div)

res=Math(384,8,6,4)
res.add()
res.subtraction()
res.multiplication()
res.division()

# 2：依靠自己的想象力，编写一个软件测试工程师类，要求包含初始化函数 类函数 对象函数  静态函数
class SoftwareTestEngineer:
    def __init__(self,work_time,salary):
        self.work_time = work_time
        self.salary = salary
    def do_sql(self):   # 对象方法
        print('会操作数据库')
        print('工作时间是：',self.work_time)  # 对象调用
    def do_linux(self):
        print('会操作Linux')
    @staticmethod   # 引入静态方法
    def do_shell():
        print('会shell脚本')
    @classmethod    # 引入类方法
    def coding(cls,code):
        print('会代码：',code)
        engineer_a.do_sql() # 对象方法，只能对象调用
    def do_api_testing(self):
        print('会接口测试')
engineer_a = SoftwareTestEngineer('3年','15000') # 实例化，创建对象
engineer_a.do_sql()
engineer_a.coding('python')
engineer_a.do_api_testing()
engineer_a.do_shell()





