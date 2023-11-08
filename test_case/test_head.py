# -*- coding: utf-8 -*-

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
import modules.router_status
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.router_status import *
from tools import *
#########################
from selenium import webdriver


def case(headChoose):
    lr = login_router()
    rst = router_status()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if headChoose == 1:
                if rst.client(driver) == 1:
                    logging.info('===================Success')
                    driver.quit()
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "client-%s.jpg" % test_time)
                    logging.info('=========================Fail')
                    driver.quit()
            if headChoose == 2:
                if rst.guanwangs(driver) == 1:
                    driver.quit()
                    return 2
                else:
                    driver.get_screenshot_as_file(caseFail + "guanwang-%s.jpg" % test_time)
                    logging.info('=========================Fail')
                    driver.quit()
    driver.quit()


def test_client():
    assert case(1) == 1

def test_guanwangs():
    assert case(2) == 2


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))