# -*- coding: utf-8 -*-

###################################
#   路由状态跳转
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import pytest
#########################
#  import module
#########################
import sys
sys.path.append("..")
import modules.login_router
import modules.router_status
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_status import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver


def case():
    lr = login_router()
    rst = router_status()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rst.Routing_state(driver, 2) == 2:
                time.sleep(5)
                if rst.Routing_state_check(driver, 2) == 2:
                    logging.info("pass")
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "devicejump-%s.jpg" % test_time)
                    logging.error('=== device jump ===Fail')
    driver.quit()


def test_devicejump():
    assert case() == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))