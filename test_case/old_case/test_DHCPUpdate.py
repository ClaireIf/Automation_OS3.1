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
    filename = os.path.basename(__file__).split('.')[0]
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    dns3 = config.get('DHCP', 'dns3')
    dns4 = config.get('DHCP', 'dns4')
    new_build = config.get('Upgrade', 'new_build')
    upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 2) == 2:
                time.sleep(2)
                if rs.setDHCP(driver, 1, dns3, dns4) == 1:
                    #####进行升级#####
                    if rs.setup_choose(driver, 5) == 5:
                        if rs.upgrade(driver, new_build, upgrade_wtime) == 1:
                            if lr.open_url(driver, 'http://'+default_ip) == 1:
                                if lr.login(driver, default_pw) == 1:
                                    if rs.setup_choose(driver, 2) == 2:
                                        time.sleep(2)
                                        if rs.getDHCP(driver, dns3, dns4) == 1:
                                            logging.info('=== DHCP Update Success ===')
                                            driver.quit()
                                            return 1
                                        else:
                                            driver.get_screenshot_as_file(caseFail + "DHCPUpdate-%s.jpg" % test_time)
                                            logging.warning('=== DHCP Update Fail ===')
    driver.quit()


def test_do():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))