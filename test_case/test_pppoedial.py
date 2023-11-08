# -*- coding:utf-8 -*-
###################################
#   互联网网设置pppoe拨号
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
    lr=login_router()
    rs=router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    pppoe_user = config.get('PPPOE', 'pppoe_user')
    pppoe_pw = config.get('PPPOE','pppoe_pw' )
    b ='www.baidu.com'
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 2) == 2:
                if rs.pppoes(driver, pppoe_user, pppoe_pw) == 1:
                    time.sleep(20)
                    p = os.system("ping %s" % b)
                    if p == 0:
                        print('ok')
                        return 1
                        driver.close()
                    else:
                        return 0
                        driver.close()
                        logging.warning("===test ping fail ===")
                else:
                    logging.warning("===test fail pppoes")
                    return 0
                    driver.close()
            else:
                logging.warning("===test fail jy===")
                return 0
                driver.close()
        else:
            logging.warning("===test fail login===")
            return 0
            driver.close()
    else:
        logging.warning("===test fail open url===")
        return 0
        driver.close()


def test_do():
    assert case() == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))

