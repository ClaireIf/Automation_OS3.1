# -*- coding: utf-8 -*-
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
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from tools import *
#########################
from selenium import webdriver


def case():
    lr = login_router()
    rs = router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 5) == 5:
                if rs.restart(driver, restart_wtime) == 1:
                    if t.urlRequest(default_ip) == 1:
                        logging.info("=============Success")
                        if t.urlRequest('www.baidu.com') == 1:
                            logging.info('===================Ping Success')
                            driver.quit()
                            return 1
                        else:
                            driver.get_screenshot_as_file(caseFail + "restart2-%s.jpg" % test_time)
                            logging.warning("==================Ping Fail")
                    else:
                        driver.get_screenshot_as_file(caseFail + "restart1-%s.jpg" % test_time)
                        logging.warning("restart ping default ip fail==")
    driver.quit()


def test_restart():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))