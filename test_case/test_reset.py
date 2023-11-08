# -*- coding:utf-8 -*-
###################################
#   系统设置恢复出厂置
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import pytest
import conftest
#########################
#  import module
#########################
import sys
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize_new
from modules.login_router import *
from modules.router_setup import *
from modules.initialize_new import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
caseFail = projectpath + '/errorpng/caseFail/'
test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
reset_wtime = int(config.get('Reset', 'reset_time'))
logging.info(__file__)

def check_reset(driver):
    if lr.open_url(driver, 'http://' + default_ip) == 2:
        logging.info('====================Reset Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "Reset-%s.jpg" % test_time)
        logging.info('========================Reset Fail')

class Test_Reset:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://'+default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 5) == 5:
                    if rs.reset(self.driver, reset_wtime) == 1:
                        pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()


    def test_reset(self):
        print('测试重置路由器')
        assert check_reset(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
