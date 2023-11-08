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


def case():
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
    SpecialChar_pw = config.get('Password', 'specialChar')
    reset_wtime = int(config.get('Reset', 'reset_time'))
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, SpecialChar_pw) == 1:
            if rs.setup_choose(driver, 5) == 5:
                if rs.reset(driver, reset_wtime) == 1:
                    if lr.open_url(driver, 'http://' + default_ip) == 2:
                        logging.info('====================Success')
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "Reset-%s.jpg" % test_time)
                        logging.info('========================Fail')
    driver.quit()


def test_reset():
    print('测试重置路由器')
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
