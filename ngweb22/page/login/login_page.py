# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/6

from selenium import webdriver
from common.base import Base
from config.data.data import data
from config.data.getcwd import get_cwd
from config.log import log

'''数据获取'''
data = data(get_cwd)
class Loggin(Base):
    '''
    元素定位:
       loc_name = 输入框
       loc_pwd = 密码框
       loc_button = 登录
    '''
    loc_name = ('xpath', '//input[@formcontrolname="userName"]')
    loc_pwd = ('xpath', '//input[@type="password"]')
    loc_button = ('xpath', '//button[contains(.,"登录")]')
    '''错误账号密码'''
    loc_prompt = ('xpath', '//span[text()="无此用户信息或是密码错误"]')
    '''账号密码为空'''
    loc_hint = ('xpath', '//div[text()="请输入密码!"]')
    loc_bug3 = ('xpath', '//div[text()="请输入用户名!"]')
    loc_bug4 = ('xpath', '//a[text()]')

    '''输入错误账号和密码'''
    def loggin(self):
        log.info('==========登陆浏览器===========')
        self.driver.get('http://192.168.1.84:4200')
        self.driver.maximize_window()
        log.info('===========输入账号密码==============')
        self.send_keys(self.loc_name, data['name'])
        self.send_keys(self.loc_pwd, data['password'])
        self.click(self.loc_button)

    def loggin_open(self):
        log.info('==========登陆浏览器===========')
        self.driver.get('http://192.168.1.84:4200')
        self.driver.maximize_window()
    def loggin_name(self):
        log.info('===========输入账号==============')
        self.send_keys(self.loc_name, data['names'])
    def loggin_pwd(self):
        log.info('============输入密码================')
        self.send_keys(self.loc_pwd, data['pwd'])
    def loggin_button(self):
        log.info('=============点击登陆=================')
        self.click(self.loc_button)
    '''下面是验证'''
    def loggin_bug1(self, _text):
        return self.is_text(self.loc_hint, _text)

    def loggin_bug2(self, _text):
        return self.is_text(self.loc_prompt, _text)

    def loggin_bug3(self, _text):
        return self.is_text(self.loc_bug3, _text)

    def loggin_bug4(self, _text):
        return self.is_text(self.loc_bug4,_text)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = Loggin(driver)
    test.loggin_open()
    test.loggin_name()
    test.loggin_pwd()
    test.loggin_button()
    # r1=test.is_text(loc_hint, "请输入密码!")
    t1="无此用户信息或是密码错误"
    r2 = test.loggin_bug2(t1)
    print(r2)

    # title="请输入密码!"
    # r1=test.loggin_prompt(title)
    # print(r1)

    quit()
