# -*- coding: utf-8 -*-
###################
##新版初始化-DHCP
###################

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
default_ssid = config.get('Default', 'default_ssid')
logging.info(__file__)

def getDefaultSSID(driver):
    return setup.getssid(driver, default_ssid)

class Test_Initialize_get_DefaultSSID:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 2:
            if setup.homepageD1(self.driver) == 1:
                pass

    def teatdown(self):
        self.driver.close()
        self.driver.quit()

    def test_get_DefaultSSID(self):
        print('测试设置向导获取默认SSID')
        assert getDefaultSSID(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))