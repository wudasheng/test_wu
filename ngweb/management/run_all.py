# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/8


import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner

casePath = "D:\\automatic\\ngweb\\case"

rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)

reportPath = "D:\\automatic\\ngweb\\report\\"+"report.html"

fp = open(reportPath, "wb")

runner = HTMLTestRunner(stream=fp,
                        title="安佳云健康测试报告",
                        description="执行云健康项目所有的测试用列而生成的报告文件")

runner.run(discover)
fp.close()
