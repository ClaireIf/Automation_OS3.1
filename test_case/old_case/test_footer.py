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



def case(footerChoose):
    lr = login_router()
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
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if footerChoose ==1:
            if lr.guanwang(driver) == 1:
                driver.quit()
                return 1
            else:
                driver.get_screenshot_as_file(caseFail + "guanwang-%s.jpg" % test_time)
                driver.quit()
        if footerChoose ==2:
            if lr.weibo(driver) == 1:
                driver.quit()
                return 2
            else:
                driver.get_screenshot_as_file(caseFail + "weibo-%s.jpg" % test_time)
                driver.quit()
        if footerChoose ==3:
            if lr.shequ(driver) == 1:
                driver.quit()
                return 3
            else:
                driver.get_screenshot_as_file(caseFail + "shequ-%s.jpg" % test_time)
                driver.quit()
    else:
        driver.quit()
    time.sleep(5)


# def test_guanwang():
#     assert case(1) == 1

def test_weibo():
    assert case(2) == 2

# def test_shequ():
#     assert case(3) ==3

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))