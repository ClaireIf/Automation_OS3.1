# -*- coding: utf-8 -*-

import logging
import os
import time
import pytest
import configparser
import sys
import conftest
sys.path.append("..")  # 引用modules模块
import modules.login_router
import modules.router_status
from modules.login_router import *
from modules.router_status import *
from tools import *
###################################
from selenium import webdriver

def case():
    lr = login_router()
    rs = router_status()
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
    mod = config.get('Default', 'model')
    ver = config.get('Upgrade', 'new_version')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.check_ver(driver, ver, mod) == 1:
                logging.info('==============Success')
                return 1
            else:
                driver.get_screenshot_as_file(caseFail + "VersionCheck-%s.jpg" % test_time)
                logging.info('==============Fail')
                return 0
    driver.quit()

def test_VersionCheck():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))