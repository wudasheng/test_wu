# - * - coding:utf-8 - * -
#author:wudasheng time:2019/3/4
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import yaml
from config.log import log
import time,os
from config.data.getcwd import get_cwd

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    '''页面一系列操作功能封装'''
    def findElement(self, locator):
        '''显示等待'''
        element = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return element

    def click(self, locator):
        '''点击操作'''
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        '''点击操作'''
        ele = self.findElement(locator)
        ele.clear()

    def send_keys(self, locator, text):
        '''输入操作'''
        send =self.findElement(locator)
        send.send_keys(text)

    def get_screenshot(self):
        '''截图操作'''
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # file = os.path.dirname(os.path.dirname(__file__))+'/picture/"+now+".jpg'
        # self.driver.get_screenshot_as_file(file)
        self.driver.get_screenshot_as_file("D:\\ngweb\\picture\\"+now+".jpg")


    '''断言封装'''
    def findElementNew(self, locator):
        '''这个是错误的等待后期从新封装'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
        return ele

    def is_tittle(self, _title):
        '''tittle封装，返回Ture和Fase'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            False

    def is_title_contains(self, _title):
        '''tittle文字包含封装，返回Ture和Fase'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text(self, locator, _text):
        '''文本封装'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def data(self, get_cwd):

        file_path = get_cwd() + r'\data_login.yaml'
        f = open(file_path, 'rb')
        y = self.yaml.load(f)  # 采用load方法读取yaml的文件内容，以json格式展示
        return y





if __name__=="__main__":
    log.info("打开浏览器")
    driver = webdriver.Chrome()
    driver.get("http://192.168.1.84:4200")
    anjia=Base(driver)
    # locl = (By.XPATH, '//input')
    # loc2 = (By.XPATH, '//input[@type="password"]')
    # loc3 = (By.XPATH, '//button[contains(.,"登录")]')
    # loc4 = (By.XPATH, '//a[contains(text(),"忘记密码")]')
    # file_path = os.path.dirname(os.path.abspath(__file__)) + r'\data_login.yaml'
    # file_path = get_cwd() + r'\data_login.yaml'
    # print(file_path)
    # f = open(file_path, 'rb')
    # y = yaml.load(f)  # 采用load方法读取yaml的文件内容，以json格式展示
    # print(y['name'])


    loc1 = ('xpath', '//input[@formcontrolname="userName"]')
    loc2 = ('xpath', '//input[@type="password"]')
    loc3 = ('xpath', '//button[contains(.,"登录")]')
    loc4 = ('xpath', '//a[contains(text(),"忘记密码")]')
    # r1 = anjia.is_tittle("安佳云健康")
    # print(r1)
    #
    # r2= anjia.is_title_contains("安佳")
    # print((r2))
    #
    r3 = anjia.is_text(loc4,"忘记密码")
    print(r3)
    # log.info('========账号==========')
    # anjia.send_keys(loc1, y['name'])
    # log.info('========判断密码输入框元素是否存在==========')
    # # anjia.findElement(loc2)
    # log.info('=========输入密码===========')
    # anjia.send_keys(loc2, '1234556')
    # anjia.click(loc3)
    quit()