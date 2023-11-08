# -*- coding: utf-8 -*-
import configparser
import logging
import os
import csv
import time
import pytest
import paramiko
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


def test_do():
    lr = login_router()
    rs = router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    new_build = config.get('Upgrade', 'new_build')
    upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
    upgrade_count = int(config.get('Upgrade', 'upgrade_count'))
    logging.info(__file__)
    for i in range(upgrade_count):
        logging.info(i)
        fail = 0
        driver = webdriver.Chrome()
        driver.maximize_window()
        if lr.open_url(driver, 'http://' + default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if rs.setup_choose(driver, 5) == 5:
                    if rs.upgrade(driver, new_build, upgrade_wtime):
                        samba = os.path.exists("S:\\")
                        logging.info('samba ===%s' % samba)
                        if samba == True:
                            logging.info("open Smaba success")
                            time.sleep(10)
                        else:
                            break
                    else:
                        driver.close()
                        continue
                else:
                    driver.close()
                    continue
            else:
                driver.close()
                continue
        else:
            driver.close()
            continue
        logging.error(fail)



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
