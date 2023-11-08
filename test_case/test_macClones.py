# -*- coding:utf-8 -*-
###################################
#   MAC克隆测试
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



def case(mChoose):
    lr = login_router()
    rs = router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
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
            if rs.setup_choose(driver, 2) == 2:
                if mChoose == 1:
                    testMac = config.get('Mac', 'terminal_mac')
                    if rs.macclone(driver, 0, testMac) == 1:
                        logging.info('========Success')
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "MacClone_Default-%s.jpg" % test_time)
                        logging.error('=========================Fail')
                if mChoose == 2:
                    testMac = config.get('Mac', 'input_mac')
                    if rs.macclone(driver, 1, testMac)== 1:
                        logging.info('========Success')
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "MacClone_input-%s.jpg" % test_time)
                        logging.error('=========================Fail')
                if mChoose == 3:
                    testMac = config.get('Mac', 'odd_mac')
                    if rs.macclone(driver, 1, testMac) ==2:
                        logging.info('========Success')
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "MacClone_inputOdd-%s.jpg" % test_time)
                        logging.error('=========================Fail')
                if mChoose == 10:
                    return rs.restore_mac(driver)
    driver.quit()

###直接点击终端MAC克隆###
def test_defaultMacClone():
    assert case(1) == 1

def test_restoreMac():
    assert case(10) ==1

def test_inputMac():
    assert case(2) == 1

def test_restore2Mac():
    assert case(10) ==1

###输入奇数###
def test_inputOddMac():
    assert case(3) == 2


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))