# -*- coding: utf-8 -*-
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


def case(Rchoose):
    lr=login_router()
    rs=router_setup()
    t =tools()
    r =relay()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    wds_pw = config.get('WDS','wds_pw')
    ra0 = 1
    rai0 = 2
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 3) == 3:
                if Rchoose == 1:
                    if r.relay(driver)==1:
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "defaultRelay-%s.jpg" % test_time)
                        logging.warning("==================Fail")
                if Rchoose == 2:
                    return r.clickRelay(driver)
                if Rchoose == 3:
                    if r.inputRelayPW(driver, wds_pw, ra0, 2) == 2:
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "relayConnCancel-%s.jpg" % test_time)
                        logging.warning("==================Fail")
                if Rchoose == 4:
                    if r.inputRelayPW(driver, wds_pw, ra0, 1) == 1:
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "relayConnSure-%s.jpg" % test_time)
                        logging.warning("==================Fail")
                if Rchoose == 5:
                    if r.clearRelay(driver, ra0, 2) !=1:
                        driver.get_screenshot_as_file(caseFail + "relayClearCancel-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                        logging.info('relayClearCancel === Fail')
                    else:
                        driver.quit()
                        return 1
                if Rchoose == 6:
                    if r.clearRelay(driver, ra0, 1) != 2:
                        driver.get_screenshot_as_file(caseFail + "relayClearSure-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                        logging.info('relayClearSure === Fail')
                    else:
                        driver.quit()
                        return 2
                if Rchoose == 7:
                    if r.inputRelayPW(driver, wds_pw, rai0, 2) !=2:
                        driver.get_screenshot_as_file(caseFail + "relay5GConnCancel-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                        logging.info('relay5GConnCancel === Fail')
                    else:
                        driver.quit()
                        return 2
                if Rchoose == 8:
                    if r.inputRelayPW(driver, wds_pw, rai0, 1) == 1:
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "relay5GConnSure-%s.jpg" % test_time)
                        logging.warning("==================Fail")
                if Rchoose == 9:
                    if r.clearRelay(driver, 2, 1) == 2:
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "relay5GClearSure-%s.jpg" % test_time)
                        logging.warning("==================Fail")
    driver.quit()


def test_defaultRelay():
    assert case(1) == 1

def test_openRelay():
    assert case(2) == 2

def test_relayConnCancel():
    assert case(3) == 2

def test_relayConnSure():
    assert case(4) == 1

def test_closeRelay():
    assert case(2) ==3

def test_reopenRelay():
    assert case(2) ==1

def test_relayClearCancel():
    assert case(5) == 1

def test_relayClearSure():
    assert case(6) == 2

def test_relay5GConnCancel():
    assert case(7) == 2

def test_relay5GConnSure():
    assert case(8) == 1

def test_relay5GClearSure():
    assert case(9) == 2

def test_closedRelay():
    assert case(2) == 3


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))