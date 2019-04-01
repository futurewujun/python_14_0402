# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 20:38
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_类与对象一.py

#类划分的标准是什么：具有相同特征 或者相同行为的一类事物
#对象  类里面的一个具体实例

#编写手机类：  特征/功能
#品牌名 价格 操作系统 颜色 尺寸
#打电话 发短信  看视频  玩游戏 拍照 听音乐 上网 读书 导航 闹钟

#对象： oppo 4500 Android 黑色 5.5
#打电话 发短信 看视频  拍照 听音乐

#python的语法
class Phone:
    '这个类是手机类，专门标记手机的属性和功能'
    brand_name='oppo'#类的属性/类的变量
    price=4500
    os='Android'
    color='black'
    size='5.5'

    #功能 类的方法
    def call(self,name='marimo'):#可以打电话 一般都是用self 对象方法
        # print('self的值:',self)
        print('可以给{}打电话'.format(name))
        return 666

    @staticmethod#静态方法
    def send_message(content):#发送短信
        #静态方法里面调用对象方法
        Phone().call()
        print('可以发送短信：{}'.format(content))

    @classmethod#类方法
    def watch_vedio(cls,*args):#看视频
        #类方法里面调用对象方法 静态方法
        cls.send_message('&&&&&&0003kdfkladfla')
        cls().call('好呀')
        Phone().call('bay_max')
        print('可以看{}'.format(args))

    def take_shot(self):#拍照---》对象方法里面调用静态方法 类方法的用法
        self.send_message('晚上好')
        self.watch_vedio('葫芦娃')
        self.call()
        print('可以拍照')

    def music(self):#可以听歌
        print('可以听歌')

    def phone_info(self):#描述手机
        print('手机的品牌是{}，价格是{}，颜色是{}，操作系统是{}'.
              format(self.brand_name,Phone.price,self.color,Phone.os))

#对象-->创建对象：类名()
# p=Phone()
#通过对象访问他的属性 对象.属性名
#结论：只能通过类和对象可以直接访问属性，并且获得他们的值#！！！！！
# print('品牌名：',p.brand_name)
# print('价格：',p.price)
# print('颜色：',p.color)
# print('品牌名:',Phone.brand_name)

#类里面的方法：对象.方法名()
#self是什么东西  对象本身
# print('p的值:',p)
# p.call()
#1:对象方法：只能通过对象来访问#！！！！！
#2:静态方法：@staticmethod 放在函数上面 来标记/装饰
#可以通过类以及对象来访问#！！！！！
# Phone.send_message()
# p.send_message()
#3:类方法：@classmethod 放在函数上面 来标记/装饰
#可以通过类以及对象来访问#！！！！！
# Phone.watch_vedio()
# p.watch_vedio()

#类的方法和普通函数有啥区别呢？
#1:除了对象方法必须有self 类方法必须有cls 参数以外，其他的并无区别
#参数类型:位置参数 默认参数 关键字参数 动态参数都有
#return 都支持
#2:必须通过该类的对象或者是该类来访问 不能直接访问
# print(p.call())
# p.send_message('你好')
# p.watch_vedio('将夜','格林童话','火王')
# p.phone_info()
# p.take_shot()
# p.send_message('7777777777777777777')

t=Phone()
t.send_message('999999999999999')
t.watch_vedio()