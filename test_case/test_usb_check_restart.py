# -*- coding: utf-8 -*-
import configparser
import logging
import os
import csv
import time
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


def case():
    # lr = login_router()
    # rs = router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    #restart_wtime = int(config.get('Restart', 'restart_wtime'))
    cmd = 'reboot'
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    time.sleep(1)
    driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
    driver.quit()
    t.ssh_cmd(default_ip,default_pw,cmd,2)
    time.sleep(360)
    samba = os.path.exists("S:\\")
    logging.info('samba ===%s' % samba)
    if samba == True:
        return 1
        logging.info("open Smaba success")
    else:
        return 0
        logging.error("open Smaba fail")


def test_do():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))