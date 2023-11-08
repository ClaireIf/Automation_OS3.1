# -*- coding: utf-8 -*-

###################################
#   路由状态跳转
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import pytest
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_status
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_status import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rst = router_status()
t = tools()
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
logging.info(__file__)

def click_terminal(driver):
    if rst.Routing_state(driver, 2) == 2:
        time.sleep(5)
        if rst.Routing_state_check(driver, 2) == 2:
            logging.info("pass")
            return 1
        else:
            driver.get_screenshot_as_file(caseFail + "devicejump-%s.jpg" % test_time)
            logging.error('=== device jump ===Fail')
            return 0

def click_internet(driver):
    if rst.Routing_state(driver, 1) == 1:
        time.sleep(5)
        if rst.Routing_state_check(driver, 1) == 1:
            logging.info("pass")
            return 1
        else:
            driver.get_screenshot_as_file(caseFail + "intelnetjump-%s.jpg" % test_time)
            logging.warning("===============================fail")
            return 0

class Test_Jumps:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://'+default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_click_terminal(self):
        print(u'测试点击终端设备')
        assert click_terminal(self.driver) == 1

    def test_click_internet(self):
        print(u'测试点击互联网')
        assert click_internet(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))