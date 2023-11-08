# -*- coding:utf-8 -*-
###################################
#   测试页脚
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
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
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
logging.info(__file__)

class Test_Footer:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_guanwang(self):
        assert lr.guanwang(self.driver) == 1

    def test_weibo(self):
        assert lr.weibos(self.driver) == 1

    def test_shequ(self):
        assert lr.shequ(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))