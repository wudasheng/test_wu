# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/7
import unittest
from selenium import webdriver
from page.login.login_page import Loggin
from config.log import log
from common.base import Base
from time import sleep

class Test_Loggin(unittest.TestCase,Base):
    '''登录用列'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.open = Loggin(cls.driver)

    def setUp(self):
        self.open.loggin_open()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        sleep(2)

    def test1(self):
        '''错误账号密码'''
        log.info('===========test1错误账号密码===============')
        self.open.loggin_name()
        self.open.loggin_pwd()
        self.open.loggin_button()
        log.info('============验证提示信息==========')
        t1="无此用户信息或是密码错误"
        verify = self.open.loggin_bug2(t1)
        self.assertTrue(verify)
        log.info('==========判断成功================')

    def test2(self):
        ''' 账号密码为空 '''
        log.info('============test2账号密码为空==================')
        self.open.loggin_button()
        t3 = "请输入用户名!"
        t4 = "请输入密码!"
        verify1=self.open.loggin_bug3(t3)
        verify2=self.open.loggin_bug1(t4)
        self.assertTrue(verify1)
        log.info('=========错误用户名提示验证成功============')
        self.assertTrue(verify2)

    def test3(self):
        '''正常用户登陆'''
        log.info('===============test3正常用户登陆=====================')
        self.open.loggin()
        sleep(3)
        tt = "吴大胜"
        self.assertTrue(tt)
        log.info('==========用户正常登陆成功===========')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()




