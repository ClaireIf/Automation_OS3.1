# -*- coding: utf-8 -*-

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
import modules.device_management
from modules.login_router import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

def case(speedChoose):
    lr = login_router()
    t = tools()
    dm = device_management()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    up = config.get('Qos', 'up_limit')
    down = config.get('Qos', 'down_limit')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if speedChoose == 1:
                if dm.devicesManagement(driver, 2) == 2:
                    if dm.testSpeed(driver) == 1:
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "testSpeed-%s.jpg" % test_time)
                        logging.error('=========================Fail')
                        return 0
            else:
                if dm.devicesManagement(driver, 2) == 3:
                    if speedChoose ==2:
                        if dm.resurveySpeed(driver)==1:
                            driver.quit()
                            return 2
                        else:
                            driver.get_screenshot_as_file(caseFail + "resurveySpeed-%s.jpg" % test_time)
                            logging.error('=========================Fail')
                            return 0
                    if speedChoose ==3:
                        if dm.editSpeed(driver, up, down, 2)==2:
                            driver.quit()
                            return 3
                        else:
                            driver.get_screenshot_as_file(caseFail + "CancelSaveSpeed-%s.jpg" % test_time)
                            logging.error('=========================Fail')
                            return 0
                    if speedChoose ==4:
                        if dm.editSpeed(driver, up, down, 1)==1:
                            driver.quit()
                            return 4
                        else:
                            driver.get_screenshot_as_file(caseFail + "SureSaveSpeed-%s.jpg" % test_time)
                            logging.error('=========================Fail')
                            return 0
                    if speedChoose ==5:
                        if dm.closeSpeed(driver)==1:
                            driver.quit()
                            return 5
                        else:
                            driver.get_screenshot_as_file(caseFail + "closeSpeed-%s.jpg" % test_time)
                            logging.error('=========================Fail')
                            return 0
    driver.quit()


def test_testSpeed():
    assert case(1) ==1

def test_resurveySpeed():
    assert case(2) ==2

def test_CancelSaveSpeed():
    assert case(3) ==3

def test_SureSaveSpeed():
    assert case(4) ==4

def test_closeSpeed():
    assert case(5) ==5

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


