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
import modules.router_setup
import modules.initialize
from modules.login_router import *
from modules.initialize_new import *
from modules.router_setup import *
from modules.wifi import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
w = wifi()
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
test_ssid = config.get('SSID', 'ssid_number')
logging.info(__file__)
ra0 = 1
rai0 = 2

def get_24g_newSSID(driver):
    logging.info('================%s' % test_ssid)
    if w.getSSID(driver, ra0, test_ssid) == 1:
        logging.info('==============success===========')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefaulte24SSID-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_5g_newSSID(driver):
    if w.getSSID(driver, rai0, test_ssid+'_5G') == 2:
        logging.info('=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "getDefaulte5SSID-%s.jpg" % test_time)
        logging.warning('============================Fail')

class Test_get_NEWSSID:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 1) == 1:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_get_24G_Number_SSID(self):
        print(u'初始化设置-获取纯数字 2.4G SSID')
        assert get_24g_newSSID(self.driver) == 1

    def test_get_5G_Number_SSID(self):
        print(u'初始化设置-获取纯数字 5G SSID')
        assert get_5g_newSSID(self.driver) == 2

