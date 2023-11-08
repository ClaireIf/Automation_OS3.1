# -*- coding: utf-8 -*-
###################
##新版初始化-DHCP
###################

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
import modules.initialize
from modules.login_router import *
from modules.initialize_new import *
from tools import *
#########################
from selenium import webdriver


def case():
    lr = login_router()
    setup = initialize()
    t=tools()
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
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 2:
        if setup.homepage(driver) == 1:
            if setup.initialize_pw(driver, default_pw) == 1:
                if setup.complete(driver) == 1:
                    driver.quit()
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "setupDHCPNew-%s.jpg" % test_time)
                    logging.warning('=========================Fail')
                    return 0
    driver.quit()

def test_setupDHCPNew():
    assert case() == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))