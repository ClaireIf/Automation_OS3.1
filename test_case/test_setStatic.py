# -*- coding:utf-8 -*-
###################################
#   互联网设置静态IP
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import csv
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


def case(test_statics):
    lr = login_router()
    rs = router_setup()
    t = tools()
    filename = os.path.basename(__file__).split('.')[0]
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    ipaddr = config.get('Static', 'ipaddr')
    netmask = config.get('Static', 'netmask')
    gateway = config.get('Static', 'gateway')
    dns1 = config.get('Static', 'dns1')
    dns2 = config.get('Static', 'dns2')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 2) == 2:
                time.sleep(2)
                if rs.set_statics(driver, test_statics, ipaddr, netmask, gateway, dns1, dns2) == 1:
                    driver.quit()
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "setupD1DHCPNew-%s.jpg" % test_time)
                    logging.warning('=========================Fail')
                    return 0
    driver.quit()


def test_setStaticFill():
    assert case(1) == 1

def test_setStaticAll():
    assert case(2) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))