'''
Created on Jan 8, 2019

@author: dwq
'''

#===============================================================================
# 7、写一个餐厅菜单显示程序：（大概的设计模式如下） 请自己设计一个数据存储这些菜单，
# 然后根据你从客户端输入的数据去进行菜名的读取。
# 比如说当我输入:平价菜中的苦瓜炒肉，就会显示有这道菜以及价格，否则就显示不存在这道菜。
#===============================================================================

menu = {'平价菜':
            {'手撕包菜':10, '苦瓜炒蛋':12},
        '凉菜':
            {'凉拌黄瓜':8},
        '小锅现炒':
            {'大盆花菜':16}
       }


#===============================================================================
# 列出整个菜单
#===============================================================================
def listMenu():
    for categoryName in menu:
        print("************{}**********".format(categoryName))
        category = menu[categoryName]
        for dishName in category:
            print("{}\t{}".format(dishName, category[dishName]))


#===============================================================================
# 根据种类、菜名 查找某道菜
#===============================================================================
def search(searchCategoryName, searchDishName):
    if searchCategoryName in menu and searchDishName in menu[searchCategoryName]:
        print("{}中的'{}'的价格是 {}".format(searchCategoryName, searchDishName, menu[searchCategoryName][searchDishName]))
    else:
        print("sorry，没有{}'{}'".format(searchCategoryName, searchDishName))
            
            
#===============================================================================
# 根据菜名 查找某道菜
#===============================================================================
def searchByDishName(searchDishName):
    flag = False
    for categoryName in menu:
        category = menu[categoryName];
        for dishName in category:
            if(dishName == searchDishName):
                print("我们有 {}中的'{}'，价格是{}".format(categoryName, dishName, category[dishName]))
                flag = True
    if flag == False:
        print("sorry，没有{}这道菜".format(searchDishName))


print("=======这里是我们的菜单=======")
listMenu()
 
while True:    
    input_search = input(
        '''
*******请点菜******        
输入格式：
（1）直接输入菜名，如 苦瓜炒蛋
（2）输入分类+菜名，如 平价菜中的苦瓜炒蛋

：'''
    )
    if len(input_search.strip()) == 0:
        print("输入不能为空，请重新输入") 
        continue
    s_arr = input_search.strip().split("中的")
    if len(s_arr) < 2:
        searchByDishName(s_arr[0])
    elif len(s_arr) == 2:
        search(s_arr[0], s_arr[1])
    else:
        print("输入格式不正确，请按照格式要求输入")
