# -*- coding: utf-8 -*-

import configparser
import logging
import time
import os

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





for i in range(100000):
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    driver = webdriver.Chrome()
    driver.get("https://online-api.xcloud.cc/router/plugins/getPlugins/firmware/3.1.0.1000/version/0.0.0.0/mac/ec:0e:c4:0f:de:73/os/xCloudOS/force/false/platform/y1/pagesize/0/p/0?callback=jQuery19106331227631308138_1460696454396&_=1460696454397")
    time.sleep(10)
    # x = driver.find_element_by_css_selector("body").text
    # print(x)
    # if x== '':
    #     logging.error("fail")
    #     driver.get_screenshot_as_file("D:\\test\\plugin%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))

    try:
        driver.find_element_by_css_selector("body").is_displayed()
        logging.info("pass")
    except Exception as e:
        driver.get_screenshot_as_file("D:\\test\\plugin_po%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
        logging.error("fail")
    driver.close()




