# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/6

import os
def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    #当前文件的绝对路径
    return path