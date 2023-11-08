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
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.wifi import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
w = wifi()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
default_24ssid = config.get('Default', 'default_ssid')
default_5ssid = default_24ssid + '_5G'
default_guest = config.get('Default', 'default_guest')
default_guestpw = config.get('Default', 'default_guestpw')
SSID24 = config.get('WiFi', 'ssid24')
SSID5 = config.get('WiFi', 'ssid5')
SSIDg = config.get('WiFi', 'ssidg')
pw24 = config.get('WiFi', 'pw24')
pw5 = config.get('WiFi', 'pw5')
pwg = config.get('WiFi', 'pwg')
ra0 = 1
rai0 = 2
guest = 3

# conftest.browser()
# driver = conftest.driver
driver = webdriver.Chrome()

def enter_wifis():
    # self.
    driver.maximize_window()
    if lr.open_url(driver, 'http://' + default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 1) == 1:
                pass

def get_Default_24g_SSID():
    enter_wifis()
    if w.getSSID(driver, ra0, default_24ssid) == 1:
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefaulte24SSID-%s.jpg" % test_time)
        logging.warning('============================Fail')


def get_Default_5g_SSID(driver):
    enter_wifis()
    if w.getSSID(driver, rai0, default_5ssid) == 2:
        logging.info('=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "getDefaulte5SSID-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Default_24g_PW(driver):
    enter_wifis()
    if w.getWP(driver, ra0, default_pw) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault24Password-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Default_5g_PW(driver):
    enter_wifis()
    if w.getWP(driver, rai0, default_pw) == 2:
        logging.info('=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault5Password-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Default_24G_Encryption(driver):
    enter_wifis()
    w.advance(driver, ra0)
    if w.getEncryption(driver, ra0) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault24GEncryption-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Default_5G_Encryption(driver):
    enter_wifis()
    w.advance(driver, rai0)
    if w.getEncryption(driver, rai0) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault5GEncryption-%s.jpg" % test_time)
        logging.warning('============================Fail')


def get_24G_Hide(driver):
    enter_wifis()
    if w.getHide(driver, ra0) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "get24Hide-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_5G_Hide(driver):
    enter_wifis()
    if w.getHide(driver, rai0) == 3:
        logging.info('=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "get5Hide-%s.jpg" % test_time)
        logging.warning('============================Fail')


def get_Default_24G_HT(driver):
    enter_wifis()
    w.advance(driver, ra0)
    if w.getHT(driver, ra0) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault24HT-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Default_5G_HT(driver):
    enter_wifis()
    ###获取5GHT模式###
    w.advance(driver, rai0)
    if w.getHT(driver, rai0) == 3:
        logging.info('=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault5HT-%s.jpg" % test_time)
        logging.warning('============================Fail')


def get_Guest(driver):
    enter_wifis()
    if w.getWiFi(driver, guest) == 3:
        logging.info('=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getGuest-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Guest_SSID(driver):
    enter_wifis()
    w.clickWiFi(driver, guest)
    if w.getSSID(driver, guest, default_guest) == 3:
        logging.info('=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getGuestSSID-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Guest_WP(driver):
    enter_wifis()
    ##获取访客密码
    if w.getWP(driver, guest, default_guestpw) == 3:
        logging.info('=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getGuestWP-%s.jpg" % test_time)
        logging.warning('============================Fail')

def get_Guest_Encryption(driver):
    enter_wifis()
    ##获取访客加密方式
    if w.getEncryption(driver, guest) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getGuestEncryption-%s.jpg" % test_time)
        logging.warning('============================Fail')











