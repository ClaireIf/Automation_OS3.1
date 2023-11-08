# -*- coding: utf-8 -*-
###################################
#   Y1初始化配置网络检测测试
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import csv
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
    setup = initialize()
    t=tools()
    projectpath = os.path.dirname(os.getcwd())
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
    if lr.open_url(driver, 'http://'+default_ip) == 2:
        if setup.homepage(driver) == 1:
            if setup.detection_dhcp(driver) == 1:
                if setup.initialize_pw(driver, default_pw) == 1:
                    if lr.open_url(driver, 'http://' + default_ip) == 1:
                        logging.info("Auto3 success")
                        return 1
                        driver.close()
                    else:
                        logging.info("Auto3 fail")
                        return 0
                        driver.close()
                else:
                    logging.info("Auto3 fail")
                    return 0
                    driver.close()
            else:
                return 0
                driver.close()
                logging.info("Auto3 fail")
        else:
            return 0
            driver.close()
            logging.info("Auto3 fail")
    else:
        return 0
        driver.close()
        logging.info("Auto3 fail")


def test_do():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))