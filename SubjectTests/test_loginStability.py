# -*- coding:utf-8 -*-
###################################
#   测试登录
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
sys.path.append("..")
import modules.router_setup
import modules.login_router
from modules.router_setup import *
from modules.login_router import *
from tools import *
#########################
from selenium import webdriver


def case():
    lr = login_router()
    t =tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    for i in range(100):
        logging.info('===run test=== %s', i+1)
        fail = 0
        driver = webdriver.Chrome()
        if lr.open_url(driver, 'http://'+default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                result = 0
                result = result + 1
                return result
            else:
                fail += 1
                logging.warning("===test fail===")
                logging.info("fail count ======== %s", fail)
                break
        else:
            fail += 1
            logging.warning("===test fail===")
            logging.info("fail count ======== %s", fail)
            continue


def test_do():
    assert case() == 100


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))