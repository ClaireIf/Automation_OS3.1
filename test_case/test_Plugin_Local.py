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

def Plugin_cancel_Install(driver):
    if p.localPlugin(driver, plugin_path, 2) == 2:
        logging.info('==================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "cancelInstallPlugin-%s.jpg" % test_time)
        logging.warning('=========================Fail')


def Plugin_Local_Install(driver):
    localresult = p.localPlugin(driver, plugin_path, 1)
    return localresult

def Plugin_uninstall(driver):
    p.installedPlugin(driver)
    if p.uninstallPlugin(driver, 1) == 1:
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "uninstallPlugin-%s.jpg" % test_time)
        logging.warning('=========================Fail')

class Test_Plugin_Local:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                p.onlinePlugin(self.driver)

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_Plugin_cancel_Install(self):
        assert Plugin_cancel_Install(self.driver) == 2

    def test_Plugin_Local_Install(self):
        assert Plugin_Local_Install(self.driver) == 1

    def test_Plugin_Cover_Install(self):
        assert Plugin_Local_Install(self.driver) == 3

    def test_Plugin_uninstall(self):
        assert Plugin_uninstall(self.driver) == 1



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


