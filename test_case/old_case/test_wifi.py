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
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.wifi import *
from tools import *
#########################
from selenium import webdriver


def case(Wchoose):
    lr = login_router()
    rs = router_setup()
    t = tools()
    w = wifi()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    logging.info(__file__)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    default_24ssid = config.get('Default', 'default_ssid')
    default_5ssid = default_24ssid+'_5G'
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
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 1) == 1:
                if Wchoose == 0:
                    ##获取2.4g ssid
                    if w.getSSID(driver, ra0, default_24ssid) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefaulte24SSID-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 34:
                    ##获取5g ssid
                    if w.getSSID(driver, rai0, default_5ssid) ==2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefaulte5SSID-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 1:
                    ##获取2.4G 密码
                    if w.getWP(driver, ra0, default_pw) ==1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefault24Password-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 2:
                    ##获取5G密码
                    if w.getWP(driver, rai0, default_pw) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefault5Password-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 3:
                    ##设置2.4G SSID
                    w.setSSID(driver, ra0, SSID24)
                    w.savewifi(driver, ra0)
                    if w.getSSID(driver, ra0, SSID24) ==1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "set24GSSID-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 4:
                    ##设置5G SSID
                    w.setSSID(driver, rai0, SSID5)
                    w.savewifi(driver, rai0)
                    if w.getSSID(driver, rai0, SSID5) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "set5GSSID-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 5:
                    ##设置2.4G密码
                    w.setWP(driver, ra0, pw24)
                    w.savewifi(driver, 1)
                    if w.getWP(driver, ra0, pw24) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "set24GPW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 6:
                    ##设置5G密码
                    w.setWP(driver, rai0, pw5)
                    w.savewifi(driver, rai0)
                    if w.getWP(driver, rai0, pw5) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "set5GPW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 7:
                    w.advance(driver, ra0)
                    if w.getEncryption(driver, ra0) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefault24GEncryption-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 8:
                    w.advance(driver, rai0)
                    if w.getEncryption(driver, rai0) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefault5GEncryption-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 9:
                    ##设置2.4G加密方式为空
                    w.advance(driver, ra0)
                    w.setEncryption(driver, ra0, 1)
                    w.savewifi(driver, ra0)
                    if w.getEncryption(driver, ra0) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "set24GNullPW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 10:
                    w.advance(driver, ra0)
                    w.setEncryption(driver, 1, 2)
                    w.setWP(driver, 1, default_pw)
                    w.savewifi(driver, 1)
                    if w.getEncryption(driver, 1) ==2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "set24GPsk2PW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 11:
                    w.advance(driver, ra0)
                    w.setEncryption(driver, 1, 3)
                    w.savewifi(driver, 1)
                    w.setWP(driver, 1, default_pw)
                    if w.getEncryption(driver, 1) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "set24Psk_Psk2PW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 12:
                    w.advance(driver, rai0)
                    w.setEncryption(driver, rai0, 1)
                    w.savewifi(driver, rai0)
                    if w.getEncryption(driver, rai0) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "set5GNullPW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 13:
                    w.advance(driver, rai0)
                    w.setEncryption(driver, rai0, 2)
                    w.setWP(driver, rai0, default_pw)
                    w.savewifi(driver, rai0)
                    if w.getEncryption(driver, rai0) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "set5GPsk2PW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 14:
                    w.advance(driver, rai0)
                    w.setEncryption(driver, 2, 3)
                    w.setWP(driver, 2, default_pw)
                    w.savewifi(driver, 2)
                    if w.getEncryption(driver, 2) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "set5Psk_Psk2PW-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 15:
                    if w.getHide(driver, ra0) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "get24Hide-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 151:
                    if w.getHide(driver, rai0) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "get5Hide-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 16:
                    w.advance(driver, ra0)
                    w.setHide(driver, ra0)
                    w.savewifi(driver, ra0)
                    if w.getHide(driver, ra0) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "set24Hide-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 17:
                    w.advance(driver, rai0)
                    w.setHide(driver, rai0)
                    w.savewifi(driver, rai0)
                    if w.getHide(driver, rai0) == 4:
                        logging.info('=========================Success')
                        driver.quit()
                        return 4
                    else:
                        driver.get_screenshot_as_file(caseFail + "set5Hide-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 18:
                    w.advance(driver, ra0)
                    if w.getHT(driver, ra0) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefault24HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 181:
                    ###获取5GHT模式###
                    w.advance(driver, rai0)
                    if w.getHT(driver, rai0) ==3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "getDefault5HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 19:
                    w.advance(driver, ra0)
                    w.setHT(driver, ra0, 2)
                    w.savewifi(driver, ra0)
                    if w.getHT(driver, ra0) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "setra0_40HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 20:
                    w.advance(driver, ra0)
                    w.setHT(driver, ra0, 1)
                    w.savewifi(driver, ra0)
                    if w.getHT(driver, ra0) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "setra0_2040HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 21:
                    w.advance(driver, rai0)
                    w.setHT(driver, rai0, 4)
                    w.savewifi(driver, rai0)
                    if w.getHT(driver, rai0) == 4:
                        logging.info('=========================Success')
                        driver.quit()
                        return 4
                    else:
                        driver.get_screenshot_as_file(caseFail + "setrai0_40HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 22:
                    w.advance(driver, rai0)
                    w.setHT(driver, rai0, 5)
                    w.savewifi(driver, rai0)
                    if w.getHT(driver, rai0) == 5:
                        logging.info('=========================Success')
                        driver.quit()
                        return 5
                    else:
                        driver.get_screenshot_as_file(caseFail + "setrai0_80HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 23:
                    ###设置5G 20/40HT
                    w.advance(driver, rai0)
                    w.setHT(driver, rai0, 3)
                    w.savewifi(driver, rai0)
                    if w.getHT(driver, rai0) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "setrai0_2040HT-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 25:
                    if w.getWiFi(driver, guest) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "getGuest-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 26:
                    ##获取访客SSID
                    w.clickWiFi(driver, guest)
                    if w.getSSID(driver, guest, default_guest) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "getGuestSSID-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 27:
                    ##获取访客密码
                    if w.getWP(driver, guest, default_guestpw) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "getGuestWP-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 28:
                    ##获取访客加密方式
                    if w.getEncryption(driver, guest) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "getGuestEncryption-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 29:
                    ##设置访客SSID
                    w.setSSID(driver, guest, SSIDg)
                    w.savewifi(driver, guest)
                    if w.getSSID(driver, guest, SSIDg) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "setGuestSSID-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 30:
                    ##设置访客密码
                    w.setWP(driver, guest, pwg)
                    w.savewifi(driver, guest)
                    if w.getWP(driver, guest, pwg) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "setGuestWP-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 31:
                    ##访客加密方式为空
                    w.setEncryption(driver, guest, 1)
                    w.savewifi(driver, guest)
                    if w.getEncryption(driver, guest) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "setGuestNUll-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 32:
                    ##访客加密方式PSK2
                    w.setEncryption(driver, guest, 2)
                    w.setWP(driver, guest, default_guest)
                    w.savewifi(driver, guest)
                    if w.getEncryption(driver, guest) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "setGuestPSK2-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 33:
                    ##访客加密方式PSK+PSK2
                    w.setEncryption(driver, guest, 3)
                    w.savewifi(driver, guest)
                    if w.getEncryption(driver, guest) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "setGuestPSK_PSK2-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 51:
                    w.clickWiFi(driver, ra0)
                    if w.getWiFi(driver, ra0) == 1:
                        logging.info('=========================Success')
                        driver.quit()
                        return 1
                    else:
                        driver.get_screenshot_as_file(caseFail + "close24WiFi-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 52:
                    w.clickWiFi(driver, rai0)
                    if w.getWiFi(driver, rai0) == 2:
                        logging.info('=========================Success')
                        driver.quit()
                        return 2
                    else:
                        driver.get_screenshot_as_file(caseFail + "close5WiFi-%s.jpg" % test_time)
                        logging.warning('============================Fail')
                if Wchoose == 53:
                    w.clickWiFi(driver, guest)
                    if w.getWiFi(driver, guest) == 3:
                        logging.info('=========================Success')
                        driver.quit()
                        return 3
                    else:
                        driver.get_screenshot_as_file(caseFail + "closeGuestWiFi-%s.jpg" % test_time)
                        logging.warning('============================Fail')
    driver.quit()

###获取2.4G 默认SSID###
def test_getDefaulte24SSID():
    assert case(0) == 1

###获取 5G 默认SSID###
def test_getDefault5SSID():
    assert case(34) == 2

### 获取2.4G 默认密码 ###
def test_getDefault24Password():
    assert case(1) == 1

### 获取5G 默认密码###
def test_getDefault5Password():
    assert case(2) == 2

### 获取2.4G默认加密类型 ###
def test_getDefault24GEncryption():
    assert case(7) == 1

def test_getDefault5GEncryption():
    assert case(8) ==1

def test_set24GSSID():
    assert case(3) == 1

def test_set5GSSID():
    assert case(4) == 2

def test_set24GPW():
    assert case(5) == 1

def test_set5GPW():
    assert case(6) == 2

def test_set24GNullPW():
    assert case(9) == 3

def test_set24GPsk2PW():
    assert case(10) == 2

def test_set24Psk_Psk2PW():
    assert case(11) == 1

def test_set5GNullPW():
    assert case(12) == 3

def test_set5GPsk2PW():
    assert case(13) == 2

def test_set5Psk_Psk2PW():
    assert case(14) == 1

def test_get24Hide():
    assert case(15) == 1

def test_get5Hide():
    assert case(151) == 3

def test_set24Hide():
    assert case(16) == 2

def test_set5Hide():
    assert case(17) == 4

def test_getDefault24HT():
    assert case(18) == 1

def test_getDefault5HT():
    assert case(181) == 3

def test_setra0_40HT():
    assert case(19) == 2

def test_setra0_2040HT():
    assert case(20) == 1

def test_setrai0_40HT():
    assert case(21) == 4

def test_setrai0_80HT():
    assert case(22) == 5

def test_setrai0_2040HT():
    assert case(23) == 3

def test_getGuest():
    assert case(25) == 3

def test_getGuestSSID():
    assert case(26) == 3

def test_getGuestWP():
    assert case(27) == 3

def test_getGuestEncryption():
    assert case(28) == 1

def test_setGuestSSID():
    assert case(29) == 3

def test_setGuestWP():
    assert case(30) == 3

def test_setGuestNUll():
    assert case(31) == 3

def test_setGuestPSK2():
    assert case(32) == 2

def test_setGuestPSK_PSK2():
    assert case(33) == 1

def test_closeGuestWiFi():
    assert case(53) == 3

def test_close24WiFi():
    assert case(51) == 1

def test_close5WiFi():
    assert case(52) == 2


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))