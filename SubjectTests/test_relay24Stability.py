# -*- coding:utf-8 -*-
###################################
#   路由设置无线中继
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
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from modules.relay import *
from tools import *
#########################
from selenium import webdriver


def test_case():
    lr=login_router()
    rs=router_setup()
    rel = relay()
    t =tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    wds_pw = config.get('WDS','wds_pw')
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    testname = os.path.basename(__file__).split('.')[0]
    for i in range(300):
        logging.info('============test 2.4G Relay count ==========%s' % i)
        fail = 0
        driver = webdriver.Chrome()
        driver.maximize_window()
        if lr.open_url(driver, 'http://'+default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if rs.setup_choose(driver, 3) == 3:
                    rel.clickRelay(driver)
                    if rel.inputRelayPW(driver, wds_pw, 1, 1) == 1:
                        time.sleep(10)
                        rel.clearRelay(driver, 1, 1)
                        time.sleep(1)
                    else:
                        driver.get_screenshot_as_file(caseFail + testname +"-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                        rel.errorSure(driver)
                        fail =fail+ 1
                        logging.info("fail count ======== %s", fail)
                        logging.warning("===test fail relay")
                    rel.clickRelay(driver)
                    driver.close()
                else:
                    fail =fail+ 1
                    logging.info("fail count ======== %s", fail)
                    logging.warning("===test fail jy===")
                    driver.close()
                    continue
            else:
                fail =fail+ 1
                logging.info("fail count ======== %s", fail)
                logging.warning("===test fail login===")
                driver.close()
                continue
        else:
            fail =fail+ 1
            logging.info("fail count ======== %s", fail)
            logging.warning("===test fail open url===")
            driver.close()
            continue



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
