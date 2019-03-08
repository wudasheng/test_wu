# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/7
from config.data.getcwd import get_cwd
import yaml
import os

def data(get_cwd):

    file_path = get_cwd()+r'\data_login.yaml'
    f = open(file_path,'rb')
    y=yaml.load(f) #采用load方法读取yaml的文件内容，以json格式展示
    return y