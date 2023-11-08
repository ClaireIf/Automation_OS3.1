# -*- coding: utf-8 -*-
###################
###USB 安全拔出
###################
import configparser
import logging
import time
import os
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
import modules.router_status
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.router_status import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rst = router_status()
t = tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
logging.info(__file__)


def PullOutUSB(driver):
    if rst.PullOutUSB_D1(driver) == 1:
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "pullD1OutUSB-%s.jpg" % test_time)
        logging.warning('=========================Fail')
        return 2


class Test_PullOut:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_pullD1OutUSB(self):
        assert PullOutUSB(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
