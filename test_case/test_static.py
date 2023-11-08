# -*- coding:utf-8 -*-
###################################
#   互联网设置静态IP
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import paramiko
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
new_build = config.get('Upgrade', 'new_build')
new_version = config.get('Upgrade', 'new_version')
upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
restart_wtime = int(config.get('Restart', 'restart_wtime'))
test_statics = 1  ##静态ip填充测试##
logging.info(__file__)


def restart_static(driver):
    if rs.restart(driver, restart_wtime) == 1:
        if lr.open_url(driver, 'http://' + default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if rs.setup_choose(driver, 2) == 2:
                    time.sleep(2)
                    if rs.get_static(driver, ipaddr, netmask, gateway, dns1, dns2) == 5:
                        logging.info('restart_static===========Case Success')
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "staticRestart-%s.jpg" % test_time)
                        logging.warning('restart_static===================Case Fail')


def upgrade_static(driver):
    if rs.upgrade(driver, new_build, upgrade_wtime) ==1:
        if lr.open_url(driver, 'http://' + default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if rs.setup_choose(driver, 2) == 2:
                    time.sleep(2)
                    if rs.get_static(driver, ipaddr, netmask, gateway, dns1, dns2) == 5:
                        logging.info('upgrade_static=================Case Success')
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "staticUpdate-%s.jpg" % test_time)
                        logging.warning('upgrade_static===================Case Fail')


class Test_SET_Static:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 2) == 2:
                    time.sleep(2)
                    if rs.set_statics(self.driver, test_statics, ipaddr, netmask, gateway, dns1, dns2) == 1:
                        if rs.setup_choose(self.driver, 5) == 5:
                            pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_Restart_Static(self):
        assert restart_static(self.driver) == 1

    def test_Upgrade_Static(self):
        assert upgrade_static(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))