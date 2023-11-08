# -*- coding: utf-8 -*-

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
import modules.initialize
from modules.login_router import *
from modules.initialize_new import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
setup = initialize()
t = tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
test_ssid = config.get('SSID', 'ssid_specialchar')
logging.info(__file__)


def setSSID(driver):
    if setup.setssid(driver, test_ssid) == 1:
        if setup.initialize_pw(driver, default_pw) == 1:
            return setup.complete(driver)

class Test_Initialize_SSID:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 2:
            if setup.homepage(self.driver) == 1:
                pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_set_special_char_SSID(self):
        print(u'测试设置初始化ssid为特殊字符')
        assert setSSID(self.driver) == 1



# if __name__ == '__main__':
#     pytest.main(os.path.basename(__file__))