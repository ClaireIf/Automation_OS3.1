# -*- coding:utf-8 -*-
###################################
#   下载系统日志
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



def case():
    lr = login_router()
    rs = router_setup()
    t = tools()
    dm = device_management()
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
    test_device = config.get('Device', 'test_device')
    #print(deviceName)
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver,default_pw) == 1:
            if dm.changeDeviceName(driver,test_device):
                if lr.open_url(driver, 'http://'+default_ip) ==1:
                    if lr.login(driver,default_pw) ==1:
                        if dm.checkDeviceName(driver, test_device)==1:
                            driver.quit()
                            return 1
                        else:
                            driver.get_screenshot_as_file(caseFail + "setDeviceName-%s.jpg" % test_time)
                            logging.warning("==================Fail")
    driver.quit()




def test_setDeviceName():
    assert case() == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))

