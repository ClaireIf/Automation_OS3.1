# -*- coding:utf-8 -*-
###################################
#   系统设置恢复出厂置
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import pytest
import csv
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
from modules.initialize_new import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver


def test_do():
    lr = login_router()
    rs = router_setup()
    t = tools()
    setup = initialize()
    filename = os.path.basename(__file__).split('.')[0]
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    reset_wtime = int(config.get('Reset', 'reset_time'))
    reset_count = int(config.get('Reset', 'reset_count'))
    logging.info(__file__)
    for i in range(reset_count):
        logging.info('===run test=== %s', i+1)
        fail = 0
        driver = webdriver.Chrome()
        if lr.open_url(driver, 'http://'+default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if rs.setup_choose(driver, 5):
                    if rs.reset(driver, reset_wtime) == 1:
                        if lr.open_url(driver, 'http://' + default_ip) == 2:
                            logging.info("reset Stability success")
                            setup.homepageD1(driver)
                            setup.initialize_pw(driver, default_pw)
                            setup.complete(driver)
                            driver.close()
                        else:
                            logging.error("reset Stability fail")
                            t.errorpng(driver, filename)
                            driver.close()
                            break
                    else:
                        fail =fail+ 1
                        logging.warning("===test fail===")
                        logging.info("fail count ======== %s", fail)
                        driver.close()
                        continue
                else:
                    fail =fail + 1
                    logging.warning("===test fail===")
                    logging.info("fail count ======== %s", fail)
                    driver.close()
                    driver.close()
                    continue
            else:
                fail = fail + 1
                logging.warning("===test fail===")
                logging.info("fail count ======== %s", fail)
                driver.close()
                continue
        else:
            fail =fail + 1
            logging.warning("===test fail===")
            logging.info("fail count ======== %s", fail)
            driver.close()
            continue


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))