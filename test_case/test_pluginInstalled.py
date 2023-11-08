# -*- coding: utf-8 -*-
##############
##插件已安装
##############


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
import modules.router_setup
import modules.initialize
import modules.device_management
import modules.plugin
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from modules.plugin import *
from tools import *
#########################
from selenium import webdriver


def case(Pchoose):
    lr = login_router()
    rs = router_setup()
    t = tools()
    p = plugin()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    plugin_path = config.get('Plugin','plugin_path')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            p.onlinePlugin(driver)
            p.installedPlugin(driver)
            if Pchoose == 1:
                if p.check_defaultapp(driver) == 1:
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "checkDefaultApp-%s.jpg" % test_time)
                    logging.error('=========================Fail')
            if Pchoose == 2:
                if p.morePlugin(driver) == 1:
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "pluginMore-%s.jpg" % test_time)
                    logging.error('=========================Fail')
    driver.quit()

def test_checkDefaultApp():
    assert case(1)==1

def test_pluginMore():
    assert case(2) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))