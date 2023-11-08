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



def case(installChoose):
    lr = login_router()
    t = tools()
    p = plugin()
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
    plugin_path = config.get('Plugin','plugin_path')
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            p.onlinePlugin(driver)
            if installChoose == 1:
                localresult=p.localPlugin(driver, plugin_path, 1)
                driver.quit()
                return localresult
            if installChoose ==2:
                if p.localPlugin(driver,plugin_path,2) == 2:
                    driver.quit()
                    return 2
                else:
                    driver.get_screenshot_as_file(caseFail + "cancelInstallPlugin-%s.jpg" % test_time)
                    logging.warning('=========================Fail')
            if installChoose ==3:
                p.installedPlugin(driver)
                if p.uninstallPlugin(driver,1) ==1:
                    driver.quit()
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "uninstallPlugin-%s.jpg" % test_time)
                    logging.warning('=========================Fail')
    driver.quit()


def test_cancelInstallPlugin():
    assert case(2) ==2

def test_installLocalPlugin():
    assert case(1) ==1

def test_coverInstallPlugin():
    assert case(1) ==3

def test_uninstallPlugin():
    assert case(3) ==1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


