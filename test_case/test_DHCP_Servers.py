# -*- coding:utf-8 -*-
###################################
#   测试DHCP服务
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
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)
config_file = projectpath + '/configure/' + 'testconfig.ini'
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')

def cancel_close_dhcp_server(driver):
    if rs.dhcpServer(driver, 2) == 2:
        os.system('ipconfig  /release')
        time.sleep(3)
        os.system('ipconfig  /renew')
        if t.urlRequest(default_ip) == 1:
            logging.info("DHCP Server Close Success")
            return 1
        else:
            driver.get_screenshot_as_file(caseFail + "serverClose-%s.jpg" % test_time)
            logging.warning("DHCP Server Close Fail")

def sure_close_dhcp_server(driver):
    if rs.dhcpServer(driver, 1) == 1:
        time.sleep(10)
        os.system('ipconfig  /release')
        time.sleep(5)
        os.system('ipconfig  /renew')
        time.sleep(10)
        if t.urlRequest(default_ip) == 0:
            logging.info("DHCP Server Close Success")
            return 1
        else:
            driver.get_screenshot_as_file(caseFail + "serverClose-%s.jpg" % test_time)
            logging.warning("DHCP Server Close Fail")


def reopen_dhcp_server(driver):
    if rs.dhcpServer(driver,0) != 0:
        os.system('RestoreIP.lnk')
        time.sleep(3)
        if t.urlRequest(default_ip) == 1:
            logging.info("DHCP Server Open Success")
            return 1
        else:
            driver.get_screenshot_as_file(caseFail + "serverReopen-%s.jpg" % test_time)
            logging.error("DHCP Server Open Fail")


class Test_DHCP_Servers:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 4) == 4:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    ####取消关闭DHCPServer####
    def test_cancelServerClose(self):
        assert cancel_close_dhcp_server(self.driver) == 1

    ####确定关闭DHCPServer####
    def test_serverClose(self):
        assert sure_close_dhcp_server(self.driver) == 1
        os.system('ChangeIP.lnk')
        time.sleep(3)

    ##重新打开DHCPServer####
    def test_serverReopen(self):
        assert reopen_dhcp_server(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))