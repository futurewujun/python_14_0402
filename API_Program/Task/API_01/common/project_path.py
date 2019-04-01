# -*- coding: utf-8 -*-
import os
# 文件的路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)
# 测试用用例的路径
case_path=os.path.join(project_path,'test_case','api_test_case.xlsx')
if __name__ == '__main__':

    print(case_path)