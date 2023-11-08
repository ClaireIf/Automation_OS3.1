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
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
filename = os.path.basename(__file__).split('.')[0]
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
dns3 = config.get('DHCP', 'dns3')
dns4 = config.get('DHCP', 'dns4')
restart_wtime = int(config.get('Restart', 'restart_wtime'))
new_build = config.get('Upgrade', 'new_build')
upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
logging.info(__file__)


def restart(driver):
    if rs.setup_choose(driver, 5) == 5:
        if rs.restart(driver, restart_wtime) == 1:
            return 1


def upgrade(driver):
    if rs.setup_choose(driver, 5) == 5:
        if rs.upgrade(driver, new_build, upgrade_wtime) == 1:
            return 1


def set_DHCP_ManualDNS(driver):
    if rs.setup_choose(driver, 2) == 2:
        if rs.setDHCP(driver, 1, dns3, dns4) == 1:
            return 1


def get_DHCP_ManualDNS(driver):
    if rs.setup_choose(driver, 2) == 2:
        time.sleep(3)
        if rs.getDHCP(driver, dns3, dns4) == 1:
            logging.info('=====================Success')
            return 1
        else:
            driver.get_screenshot_as_file(projectpath + "/errorpng/caseFail/get_DHCP_ManualDNS-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.info('=====================Fail')


class Test_DHCP_ManualDNS_Restart:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                pass


    def teardown(self):
        self.driver.close()
        self.driver.quit()


    def test_set_DHCP_ManualDNS(self):
        print(u'测试DHCP联网环境下，手动设置DNS')
        assert set_DHCP_ManualDNS(self.driver) == 1

    def test_restart(self):
        print(u'重启')
        assert restart(self.driver) == 1

    def test_Restart_DHCP_ManualDNS(self):
        print(u'测试DHCP联网环境下，DNS重启保存')
        assert get_DHCP_ManualDNS(self.driver) == 1

    def test_update(self):
        print(u'升级')
        assert upgrade(self.driver) == 1

    def test_Upgrade_DHCP_ManualDNS(self):
        print(u'测试DHCP联网环境下，DNS升级保存')
        assert get_DHCP_ManualDNS(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))