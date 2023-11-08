# -*- coding:utf-8 -*-
###################################
#   下载系统日志
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
from modules.login_router import *
from modules.router_setup import *
from tools import *
#########################
from selenium import webdriver


lr = login_router()
rs = router_setup()
t = tools()
filename = os.path.basename(__file__).split('.')[0]
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
temp = config.get('SystemLog', 'log_path')
logging.info(__file__)

def downlog(driver):
    if rs.downlog(driver, temp) == 1:
        time.sleep(3)
        logging.info("=== Downlog Success ===")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "downlog-%s.jpg" % test_time)
        logging.warning("===Downlog Fail ===")


class Test_Downlog:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 5) == 5:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_downlog(self):
        assert downlog(self.driver) == 1


if __name__ == '__main__':
   pytest.main(os.path.basename(__file__))