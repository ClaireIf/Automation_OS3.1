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
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_status import *
from modules.initialize import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver


def case():
    lr = login_router()
    rst = router_status()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rst.Routing_state(driver, 1) == 1:
                time.sleep(5)
                if rst.Routing_state_check(driver, 1) == 1:
                    logging.info("pass")
                    return 1
                else:
                    driver.get_screenshot_as_file(caseFail + "intelnetjump-%s.jpg" % test_time)
                    logging.warning("===============================fail")
                    return 0
    driver.quit()


def test_do():
    assert case() == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))