# -*- coding:utf-8 -*-
###################################
#   限制外网设置-设备管理
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



def case(aChoose):
    lr = login_router()
    dm = device_management()
    t = tools()
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    projectpath = os.path.dirname(os.getcwd())
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            logging.info("router login success")
            if dm.devicesManagement(driver, 1) == 1:
                if aChoose == 1:
                    if dm.AccessNetwork(driver) ==1:
                        if t.urlRequest('www.baidu.com') !=0:
                            driver.get_screenshot_as_file(caseFail + "AccessDevice-limitNetwork-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                            logging.error('limitNetwork === Fail')
                        else:
                            return 0
                if aChoose ==2:
                    if dm.AccessNetwork(driver) ==1:
                        if t.urlRequest('www.baidu.com') !=1:
                            driver.get_screenshot_as_file(caseFail + "AccessDevice-reopenNetwork-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                            logging.error('reopenNetwork === Fail')
                        else:
                            return 1
                if aChoose == 3:
                    if dm.AccessSamba(driver,2) ==2:
                        if t.open_smaba() ==1:
                            return 1
                        else:
                            driver.get_screenshot_as_file(caseFail + "AccessDevice-limitCancelSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
                            logging.error('limitCancelSamba === Fail')
                if aChoose ==4:
                    if dm.AccessSamba(driver,1) ==1:
                        time.sleep(60)
                        if t.open_smaba() ==0:
                            return 0
                        else:
                            driver.get_screenshot_as_file(caseFail + "AccessDevice-limitSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
                            logging.error('limitSamba === Fail')
                if aChoose ==5:
                    dm.AccessSamba(driver,None)
                    if t.open_smaba() ==1:
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "AccessDevice-limitCancelSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
                        logging.error('limitCancelSamba === Fail')

    driver.quit()



def test_NetworkSamba():
    t = tools()
    assert t.urlRequest('www.baidu.com') == 1 and t.open_smaba() == 1

def test_limitNetwork():
    assert case(1) == 0

def test_reopenNetwork():
    assert case(2) == 1

def test_limitCancelSamba():
    assert case(3) == 1

def test_limitSamba():
    assert case(4) == 0

def test_reopenSamba():
    assert case(5) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))