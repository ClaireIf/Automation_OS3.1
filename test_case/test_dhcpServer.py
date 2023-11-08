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

def case_serverClose(choose):
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 4) == 4:
                time.sleep(2)
                if rs.dhcpServer(driver,choose) !=0 :
                    os.system('ipconfig  /release')
                    time.sleep(3)
                    os.system('ipconfig  /renew')
                    if t.urlRequest(default_ip)==0:
                        logging.info("DHCP Server Close Success")
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "serverClose-%s.jpg" % test_time)
                        logging.info("DHCP Server Close Fail")
    driver.quit()

def case_serverReopen():
    os.system('ChangeIP.lnk')
    time.sleep(3)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 4) == 4:
                time.sleep(2)
                if rs.dhcpServer(driver,0)!=0:
                    os.system('RestoreIP.lnk')
                    time.sleep(3)
                    if t.urlRequest(default_ip)==1:
                        logging.info("DHCP Server Open Success")
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "serverReopen-%s.jpg" % test_time)
                        logging.error("DHCP Server Open Fail")
    driver.quit()



####取消关闭DHCPServer####
def test_cancelServerClose():
    assert case_serverClose(2) == 0

####确定关闭DHCPServer####
def test_serverClose():
    assert case_serverClose(1) == 1

##重新打开DHCPServer####
def test_serverReopen():
    assert case_serverReopen() == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))