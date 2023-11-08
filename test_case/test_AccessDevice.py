# -*- coding:utf-8 -*-
###################################
#   限制外网设置-设备管理
#   配置在testconfig.ini中
###################################

import configparser
import logging
import os
import time
import csv
import pytest
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
dm = device_management()
t = tools()
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
projectpath = os.path.dirname(os.getcwd())
caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
config_file = projectpath + '/configure/' + 'testconfig.ini'
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
# logging.info(__file__)

def AccessNetwork(driver):
    if dm.AccessNetwork(driver) == 1:
        if t.urlRequest('www.baidu.com') != 0:
            driver.get_screenshot_as_file(caseFail + "AccessDevice-limitNetwork-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('limitNetwork === Fail')
        else:
            return 0

def Reopen_Network(driver):
    if dm.AccessNetwork(driver) == 1:
        if t.urlRequest('www.baidu.com') != 1:
            driver.get_screenshot_as_file(caseFail + "AccessDevice-reopenNetwork-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('reopenNetwork === Fail')
        else:
            logging.info("Reopen_Network =============Success")
            return 1

def Cancel_Limit_Samba(driver):
    if dm.AccessSamba(driver, 2) == 2:
        if t.open_smaba() == 1:
            logging.info("Cancel_Limit_Samba =============Success")
            return 1
        else:
            driver.get_screenshot_as_file(caseFail + "AccessDevice-limitCancelSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('Cancel_Limit_Samba ========== Fail')

def Limit_Samba(driver):
    if dm.AccessSamba(driver, 1) == 1:
        time.sleep(60)
        if t.open_smaba() == 0:
            logging.info("Limit_Samba =============Success")
            return 0
        else:
            driver.get_screenshot_as_file(caseFail + "AccessDevice-limitSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('limitSamba ========== Fail')

def Reopen_Samba(driver):
    dm.AccessSamba(driver, None)
    if t.open_smaba() == 1:
        logging.info("Reopen_Samba =============Success")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "AccessDevice-limitCancelSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
        logging.error('limitCancelSamba === Fail')


class Test_AccessDevices:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                logging.info("router login success")
                if dm.devicesManagement(self.driver, 1) == 1:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_NetworkSamba(self):
        t = tools()
        assert t.urlRequest('www.baidu.com') == 1 and t.open_smaba() == 1

    def test_limitNetwork(self):
        print(u'限制网络访问')
        assert AccessNetwork(self.driver) == 0

    def test_Reopen_Network(self):
        print(u'重新打开网络访问')
        assert Reopen_Network(self.driver) == 1

    def test_Cancel_Limit_Samba(self):
        print(u'取消限制访问samba')
        assert Cancel_Limit_Samba(self.driver) == 1

    def test_limitSamba(self):
        print(u'确定限制访问Samba')
        assert Limit_Samba(self.driver) == 0

    def test_reopenSamba(self):
        print(u'重新打开samba访问')
        assert Reopen_Samba(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))