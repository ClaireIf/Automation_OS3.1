# -*- coding:utf-8 -*-
###################################
#   系统状态信息检查
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import sys
import time
import csv
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
    t =tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    lan_mac = config.get('SystemInfo', 'lan_mac')
    lan_ip = config.get('SystemInfo', 'lan_ip')
    mask = config.get('SystemInfo', 'mask')
    wifi24_status = config.get('SystemInfo', 'wifi24_status')
    wifi24_ssid = config.get('SystemInfo', 'wifi24_ssid')
    wifi24_channel = config.get('SystemInfo', 'wifi24_channel')
    wifi_guest = config.get('SystemInfo', 'wifi_guest')
    wifi5_status = config.get('SystemInfo', 'wifi5_status')
    wifi5_ssid = config.get('SystemInfo', 'wifi5_ssid')
    wifi5_channel = config.get('SystemInfo', 'wifi5_channel')
    wan_status = config.get('SystemInfo', 'wan_status')
    wan_mac = config.get('SystemInfo', 'wan_mac')
    wan_ip = config.get('SystemInfo', 'wan_ip')
    gate = config.get('SystemInfo', 'gate')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        pass
    else:
        logging.info("===test fail open url===")
    if lr.login(driver, default_pw) == 1:
        pass
    else:
        logging.info("===test fail login===")
    if rs.setup_choose(driver, 5) == 5:
        pass
    else:
        logging.info("===test fail setup choose===")
    detail = rs.displaySystemInfo(driver)
    logging.info(detail)
    result = 0
    if detail[0] == lan_mac:
        logging.info("===test success, LAN MAC is right===")
        result=result+1
    else:
        logging.warning("===test fail, LAN MAC===")
    if detail[1] == lan_ip:
        result = result + 1
        logging.info("===test success, LAN IP is right===")
    else:
        logging.warning("===test fail, LAN IP===")
    if detail[2] == mask:
        result=result+1
        logging.info("===test success, mask is right===")
    else:
        logging.warning("===test fail, mask===")
    if detail[3] == wifi24_status:
        result=result+1
        logging.info("===test success, 2.4G status is right===")
    else:
        logging.warning("===test fail, 2.4G status===")
    if detail[4] == wifi24_ssid:
        result=result+1
        logging.info("===test success, 2.4G ssid is right===")
    else:
        logging.warning("===test fail, 2.4G ssid===")
    if detail[5] == wifi24_channel:
        result=result+1
        logging.info("===test success, 2.4G channel is right===")
    else:
        logging.warning("===test fail, 2.4G channel===")
    if detail[6] == wifi5_status:
        result=result+1
        logging.info("===test success, 5G status is right===")
    else:
        logging.warning("===test fail, 5G status===")
    if detail[7] == wifi5_ssid:
        result=result+1
        logging.info("===test success, 5G ssid is right===")
    else:
        logging.warning("===test fail, 5G ssid===")
    if detail[8] == wifi5_channel:
        result = result+1
        logging.info("===test success, 5G channel is right===")
    else:
        logging.warning("===test fail, 5G channel===")
    if detail[9] == wan_status:
        result = result+1
        logging.info("===test success, WAN status is right===")
    else:
        logging.warning("===test fail, WAN status===")
    if detail[10] == wan_mac:
        result=result+1
        logging.info("===test success, WAN MAC is right===")
    else:
        logging.warning("===test fail, WAN MAC===")
    if detail[11] == wan_ip:
        result=result+1
        logging.info("===test success, WAN IP is right===")
    else:
        logging.warning("===test fail, WAN IP===")
    if detail[12] == gate:
        result=result+1
        logging.info("===test success, gate is right===")
    else:
        logging.warning("===test fail, gate===")
    logging.info(result)
    if result == 13:
        logging.info('==System info success')
        return 1
    else:
        logging.error('==System info fail')
        return 0
    driver.close()

def test_do():
    assert case() == 1

if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))
