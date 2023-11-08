# -*- coding:utf-8 -*-
###################################
#  测试重启时WiFi启动
###################################
import configparser
import logging
import os
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
    restart_count = int(config.get('Restart', 'restart_count'))
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    for i in range(restart_count):
        logging.info('===run test=== %s', i+1)
        fail = 0
        driver = webdriver.Chrome()
        if lr.open_url(driver, 'http://'+default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if rs.setup_choose(driver, 5):
                    if rs.restart(driver, restart_wtime):
                        if t.urlRequest('www.baidu.com') == 1:
                            logging.info("restart Stability success")
                        else:
                            pytest.fail("restart Stability fail")
                            t.errorpng(driver, filename)
                            break
                    else:
                        fail =fail+ 1
                        logging.warning("===test fail===")
                        logging.info("fail count ======== %s", fail)
                        continue
                else:
                    fail =fail + 1
                    logging.warning("===test fail===")
                    logging.info("fail count ======== %s", fail)
                    continue
            else:
                fail = fail + 1
                logging.warning("===test fail===")
                logging.info("fail count ======== %s", fail)
                continue
        else:
            fail =fail + 1
            logging.warning("===test fail===")
            logging.info("fail count ======== %s", fail)
            continue
        driver.close()



if __name__ == '__main__':
    # chrome = webdriver.Chrome()
    # test_do(chrome)
    # chrome.close()
    pytest.main(os.path.basename(__file__))
