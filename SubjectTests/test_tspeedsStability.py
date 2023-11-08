# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import configparser
import logging
import time
import os
import pytest
#########################
#  import module
#########################
import sys
sys.path.append("..")
import modules.login_router
import modules.device_management
from modules.login_router import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

def test_case():
    lr = login_router()
    t = tools()
    dm = device_management()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    up = config.get('Qos', 'up_limit')
    down = config.get('Qos', 'down_limit')
    logging.info(__file__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    for i in range(300):
        if lr.open_url(driver, 'http://'+default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                if dm.devicesManagement(driver, 2) == 3:
                    if dm.resurveySpeed(driver)==1:
                        pass
                    else:
                        driver.get_screenshot_as_file(caseFail + "resurveySpeed-%s.jpg" % test_time)
                        logging.error('=========================Fail')
    driver.quit()



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


