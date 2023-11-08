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
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://' + default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 5) == 5:
                if rs.upgrade(driver, new_build, upgrade_wtime):
                    logging.info(filename + "success")
                    samba = os.path.exists("S:\\")
                    logging.info('samba ===%s' % samba)
                    if samba == True:
                        logging.info("open Smaba success")
                        time.sleep(10)
                        if lr.open_url(driver, 'http://' + default_ip) == 1:
                            if lr.login(driver, default_pw) == 1:
                                try:
                                    driver.find_element_by_id("sda").is_displayed()
                                    logging.info("success")
                                    return 1
                                except:
                                    driver.get_screenshot_as_file(os.getcwd())+"/errorpng/usb_check_update-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime())
                                    logging.error("fail")
                                    return 0
    driver.quit()


def test_do():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))