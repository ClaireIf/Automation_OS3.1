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
import modules.plugin
from modules.login_router import *
from modules.router_setup import *
from modules.plugin import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
p = plugin()
t = tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
logging.info(__file__)

def check_pluginOnline(driver):
    time.sleep(15)
    try:
        driver.find_element_by_css_selector("#map > div:nth-child(1) > div.plugins-f > img.plugins-img").is_displayed()
        logging.info("====================pass")
        return 1
    except:
        driver.get_screenshot_as_file(caseFail + "pluginOnline-%s.jpg" % test_time)
        logging.warning("===================Fail")

class Test_PluginOnline:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if p.onlinePlugin(self.driver) ==1:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_pluginOnline(self):
        assert check_pluginOnline(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


