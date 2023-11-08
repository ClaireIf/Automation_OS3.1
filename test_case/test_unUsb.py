# -*- coding: utf-8 -*-
###################
###未挂载USB
###################
import configparser
import logging
import csv
import os
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
import modules.router_status
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from modules.router_status import *
from tools import *
#########################
from selenium import webdriver

def Pullout():
    lr = login_router()
    rst = router_status()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            pass


def test_USB():
    assert Pullout() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
