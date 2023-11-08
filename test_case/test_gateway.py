# -*- coding:utf-8 -*-
###################################
#   局域网设置修改网关
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
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


def case(choose, address):
    lr=login_router()
    rs=router_setup()
    t=tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    if address == 1:
        default_ip = config.get('Default', 'default_ip')
        gateway_new = config.get('LAN', 'gateway_new')
    if address == 2:
        default_ip = config.get('LAN', 'gateway_new')
        gateway_new = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 4) == 4:
                if choose == 3:
                    x = rs.getGateway(driver, default_ip, gateway_new)
                    print(x)
                    return x+2
                if rs.setGateway(driver, gateway_new, choose) != 0:
                    if t.ping(gateway_new) == 0:
                        logging.info("===set Gateway CASE succese===")
                        driver.quit()
                        return 1
                    else:
                        logging.error("===set Gateway CASE fail===")
                        driver.quit()
                        return 0
    driver.quit()


#################################
## choose = 3，获取网关；
## choose =2，取消设置网关
## choose =1，确定设置网关
#################################

def test_getDefaultGateway():
    assert case(3, 1) == 3

def test_cancelSetGateway():
    assert case(2, 1) == 0

def test_setNewGateway():
    assert case(1, 1) == 1

def test_getNewGateway():
    assert case(3, 2) == 3

def test_setDefaultGateway():
    assert case(1, 2) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))

