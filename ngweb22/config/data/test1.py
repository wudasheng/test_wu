# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/7
import yaml
import os
from config.data.data import data
from config.data.getcwd import get_cwd

# file_path = os.path.dirname(os.path.abspath(__file__))+r'\data_login.yaml'
# print(file_path)
# f = open(file_path,'rb')
# y=yaml.load(f) #采用load方法读取yaml的文件内容，以json格式展示
# print(y['name'])

data=data(get_cwd)
print(data['name'])