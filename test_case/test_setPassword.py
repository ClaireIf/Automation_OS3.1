# -*- coding:utf-8 -*-
###################################
#   修改管理密码测试
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import csv
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


def case(default_pw, new_pw):
    lr = login_router()
    rs = router_setup()
    t =tools()
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            for i in range(2):
                if rs.setup_choose(driver, 5) == 5:
                    if i == 1:
                        new_pw = config.get('Default', 'default_pw')
                    if rs.set_password(driver, default_pw, new_pw) == 1:
                        logging.info("=test %s = new password = %s" % (i, new_pw))
                        time.sleep(5)
                        if lr.login(driver, new_pw) == 1:
                            default_pw = new_pw
                            logging.info("= test %s = default password = %s" % (i, default_pw))
                            logging.info("=== Set Password Success ===")
                            return 1
                        else:
                            driver.get_screenshot_as_file(caseFail + "setPassword-%s.jpg" % test_time)
                            logging.warning("=== Set Password Fail ===")
    driver.quit()


def test_en_specialChar_num():
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_pw = config.get('Default', 'default_pw')
    new_pw = config.get('Password', 'new_pw')
    assert case(default_pw,new_pw) == 1


def test_en():
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_pw = config.get('Password', 'new_pw')
    new_pw = config.get('Password', 'en')
    assert case(default_pw,new_pw) == 1

def test_specialChar():
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_pw = config.get('Password', 'en')
    new_pw = config.get('Password', 'specialChar')
    assert case(default_pw,new_pw) == 1

def test_num():
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_pw = config.get('Password', 'specialChar')
    new_pw = config.get('Password', 'num')
    assert case(default_pw, new_pw) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))