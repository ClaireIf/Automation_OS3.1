# -* coding:utf-8 -*-
###################################
#  完成初始化配置，浏览器打开网页
###################################

import logging
import os
import time
import pytest

import sys
import conftest
sys.path.append("..")  # 引用modules模块
import modules.login_router
import modules.initialize
from modules.login_router import *
from modules.initialize import *
from tools import *
###################################
from selenium import webdriver

lr = login_router()
t = tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)

def openUrl(driver,domains):
    if lr.open_url(driver, 'http://' + domains) == 2:
        logging.info('===========================Successs')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "domainInitialize-%s.jpg" % test_time)
        logging.info('============================Fail')


class Test_DomainInitialize:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_okgoJumpInitialize(self):
        assert openUrl(self.driver,'ok.go/') == 1

    def test_wifiJumpInitialize(self):
        assert openUrl(self.driver,'wi.fi') == 1

    def test_xyuncoJumpInitialize(self):
        assert openUrl(self.driver,'xyun.co') == 1

    def test_newificomInitialize(self):
        assert openUrl(self.driver,'newifi.com') == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))



