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


def get_Default_24g_SSID(driver):
    if w.getSSID(driver, ra0, default_24ssid) == 1:
        logging.info("get_Default_24g_SSID=====================Succecss")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefaulte24SSID-%s.jpg" % test_time)
        logging.warning('get_Default_24g_SSID============================Fail')

def get_Default_5g_SSID(driver):
    if w.getSSID(driver, rai0, default_5ssid) == 2:
        logging.info('get_Default_5g_SSID=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "getDefaulte5SSID-%s.jpg" % test_time)
        logging.warning('get_Default_5g_SSID============================Fail')

def get_Default_24g_PW(driver):
    if w.getWP(driver, ra0, default_pw) == 1:
        logging.info('get_Default_24g_PW=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault24Password-%s.jpg" % test_time)
        logging.warning('get_Default_24g_PW============================Fail')

def get_Default_5g_PW(driver):
    if w.getWP(driver, rai0, default_pw) == 2:
        logging.info('get_Default_5g_PW=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault5Password-%s.jpg" % test_time)
        logging.warning('get_Default_5g_PW============================Fail')

def get_Default_24G_Encryption(driver):
    w.advance(driver, ra0)
    if w.getEncryption(driver, ra0) == 1:
        logging.info('get_Default_24G_Encryption=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault24GEncryption-%s.jpg" % test_time)
        logging.warning('get_Default_24G_Encryption============================Fail')

def get_Default_5G_Encryption(driver):
    w.advance(driver, rai0)
    if w.getEncryption(driver, rai0) == 1:
        logging.info('get_Default_5G_Encryption=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault5GEncryption-%s.jpg" % test_time)
        logging.warning('get_Default_5G_Encryption============================Fail')

def set_24G_SSID(driver):
    w.setSSID(driver, ra0, SSID24)
    w.savewifi(driver, ra0)
    if w.getSSID(driver, ra0, SSID24) == 1:
        logging.info('set_24G_SSID=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "set24GSSID-%s.jpg" % test_time)
        logging.warning('set_24G_SSID============================Fail')

def set_5G_SSID(driver):
    w.setSSID(driver, rai0, SSID5)
    w.savewifi(driver, rai0)
    if w.getSSID(driver, rai0, SSID5) == 2:
        logging.info('set_5G_SSID=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "set5GSSID-%s.jpg" % test_time)
        logging.warning('set_5G_SSID============================Fail')

def set_24G_PW(driver):
    ##设置2.4G密码
    w.setWP(driver, ra0, pw24)
    w.savewifi(driver, 1)
    if w.getWP(driver, ra0, pw24) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "set24GPW-%s.jpg" % test_time)
        logging.warning('============================Fail')

def set_5G_PW(driver):
    w.setWP(driver, rai0, pw5)
    w.savewifi(driver, rai0)
    if w.getWP(driver, rai0, pw5) == 2:
        logging.info('=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "set5GPW-%s.jpg" % test_time)
        logging.warning('============================Fail')

def set_24G_Null_PW(driver):
    ##设置2.4G加密方式为空
    w.advance(driver, ra0)
    w.setEncryption(driver, ra0, 1)
    w.savewifi(driver, ra0)
    if w.getEncryption(driver, ra0) == 3:
        logging.info('set_24G_Null_PW=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "set24GNullPW-%s.jpg" % test_time)
        logging.warning('set_24G_Null_PW============================Fail')

def set_24G_Psk2_PW(driver):
    w.advance(driver, ra0)
    w.setEncryption(driver, 1, 2)
    w.setWP(driver, 1, default_pw)
    w.savewifi(driver, 1)
    if w.getEncryption(driver, 1) == 2:
        logging.info('set_24G_Psk2_PW=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "set24GPsk2PW-%s.jpg" % test_time)
        logging.warning('set_24G_Psk2_PW============================Fail')

def set_24G_Psk_Psk2_PW(driver):
    w.advance(driver, ra0)
    w.setEncryption(driver, 1, 3)
    w.savewifi(driver, 1)
    w.setWP(driver, 1, default_pw)
    if w.getEncryption(driver, 1) == 1:
        logging.info('set_24G_Psk_Psk2_PW=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "set24Psk_Psk2PW-%s.jpg" % test_time)
        logging.warning('set_24G_Psk_Psk2_PW============================Fail')

def set_5G_Null_PW(driver):
    w.advance(driver, rai0)
    w.setEncryption(driver, rai0, 1)
    w.savewifi(driver, rai0)
    if w.getEncryption(driver, rai0) == 3:
        logging.info('set_5G_Null_PW=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "set5GNullPW-%s.jpg" % test_time)
        logging.warning('set_5G_Null_PW============================Fail')

def set_5G_Psk2_PW(driver):
    w.advance(driver, rai0)
    w.setEncryption(driver, rai0, 2)
    w.setWP(driver, rai0, default_pw)
    w.savewifi(driver, rai0)
    if w.getEncryption(driver, rai0) == 2:
        logging.info('set_5G_Psk2_PW=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "set5GPsk2PW-%s.jpg" % test_time)
        logging.warning('set_5G_Psk2_PW============================Fail')

def set_5G_Psk_Psk2_PW(driver):
    w.advance(driver, rai0)
    w.setEncryption(driver, 2, 3)
    w.setWP(driver, 2, default_pw)
    w.savewifi(driver, 2)
    if w.getEncryption(driver, 2) == 1:
        logging.info('set_5G_Psk_Psk2_PW=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "set5Psk_Psk2PW-%s.jpg" % test_time)
        logging.warning('set_5G_Psk_Psk2_PW============================Fail')

def get_24G_Hide(driver):
    if w.getHide(driver, ra0) == 1:
        logging.info('get_24G_Hide=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "get24Hide-%s.jpg" % test_time)
        logging.warning('get_24G_Hide============================Fail')

def get_5G_Hide(driver):
    if w.getHide(driver, rai0) == 3:
        logging.info('get_5G_Hide=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "get5Hide-%s.jpg" % test_time)
        logging.warning('get_5G_Hide============================Fail')

def set_24G_Hide(driver):
    w.advance(driver, ra0)
    w.setHide(driver, ra0)
    w.savewifi(driver, ra0)
    if w.getHide(driver, ra0) == 2:
        logging.info('set_24G_Hide=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "set24Hide-%s.jpg" % test_time)
        logging.warning('set_24G_Hide============================Fail')

def set_5G_Hide(driver):
    w.advance(driver, rai0)
    w.setHide(driver, rai0)
    w.savewifi(driver, rai0)
    if w.getHide(driver, rai0) == 4:
        logging.info('set_5G_Hide=========================Success')
        return 4
    else:
        driver.get_screenshot_as_file(caseFail + "set5Hide-%s.jpg" % test_time)
        logging.warning('set_5G_Hide============================Fail')

def get_Default_24G_HT(driver):
    w.advance(driver, ra0)
    if w.getHT(driver, ra0) == 1:
        logging.info('get_Default_24G_HT=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault24HT-%s.jpg" % test_time)
        logging.warning('get_Default_24G_HT============================Fail')

def get_Default_5G_HT(driver):
    ###获取5GHT模式###
    w.advance(driver, rai0)
    if w.getHT(driver, rai0) == 3:
        logging.info('get_Default_5G_HT=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getDefault5HT-%s.jpg" % test_time)
        logging.warning('get_Default_5G_HT============================Fail')

def set_ra0_40_HT(driver):
    w.advance(driver, ra0)
    w.setHT(driver, ra0, 2)
    w.savewifi(driver, ra0)
    if w.getHT(driver, ra0) == 2:
        logging.info('set_ra0_40_HT=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "setra0_40HT-%s.jpg" % test_time)
        logging.warning('set_ra0_40_HT============================Fail')

def set_ra0_2040_HT(driver):
    w.advance(driver, ra0)
    w.setHT(driver, ra0, 1)
    w.savewifi(driver, ra0)
    if w.getHT(driver, ra0) == 1:
        logging.info('set_ra0_2040_HT=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "setra0_2040HT-%s.jpg" % test_time)
        logging.warning('set_ra0_2040_HT============================Fail')

def set_rai0_40_HT(driver):
    w.advance(driver, rai0)
    w.setHT(driver, rai0, 4)
    w.savewifi(driver, rai0)
    if w.getHT(driver, rai0) == 4:
        logging.info('set_rai0_40_HT=========================Success')
        return 4
    else:
        driver.get_screenshot_as_file(caseFail + "setrai0_40HT-%s.jpg" % test_time)
        logging.warning('set_rai0_40_HT============================Fail')

def set_rai0_80_HT(driver):
    w.advance(driver, rai0)
    w.setHT(driver, rai0, 5)
    w.savewifi(driver, rai0)
    if w.getHT(driver, rai0) == 5:
        logging.info('set_rai0_80_HT=========================Success')
        return 5
    else:
        driver.get_screenshot_as_file(caseFail + "setrai0_80HT-%s.jpg" % test_time)
        logging.warning('set_rai0_80_HT============================Fail')

def set_rai0_2040_HT(driver):
    ###设置5G 20/40HT
    w.advance(driver, rai0)
    w.setHT(driver, rai0, 3)
    w.savewifi(driver, rai0)
    if w.getHT(driver, rai0) == 3:
        logging.info('set_rai0_2040_HT=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "setrai0_2040HT-%s.jpg" % test_time)
        logging.warning('set_rai0_2040_HT============================Fail')

def get_Guest(driver):
    if w.getWiFi(driver, guest) == 3:
        logging.info('get_Guest=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getGuest-%s.jpg" % test_time)
        logging.warning('get_Guest============================Fail')

def get_Guest_SSID(driver):
    w.clickWiFi(driver, guest)
    if w.getSSID(driver, guest, default_guest) == 3:
        logging.info('get_Guest_SSID=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getGuestSSID-%s.jpg" % test_time)
        logging.warning('get_Guest_SSID============================Fail')

def get_Guest_WP(driver):
    ##获取访客密码
    if w.getWP(driver, guest, default_guestpw) == 3:
        logging.info('get_Guest_WP=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "getGuestWP-%s.jpg" % test_time)
        logging.warning('get_Guest_WP============================Fail')

def get_Guest_Encryption(driver):
    ##获取访客加密方式
    if w.getEncryption(driver, guest) == 1:
        logging.info('=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "getGuestEncryption-%s.jpg" % test_time)
        logging.warning('============================Fail')

def set_Guest_SSID(driver):
    ##设置访客SSID
    w.setSSID(driver, guest, SSIDg)
    w.savewifi(driver, guest)
    if w.getSSID(driver, guest, SSIDg) == 3:
        logging.info('set_Guest_SSID=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "setGuestSSID-%s.jpg" % test_time)
        logging.warning('set_Guest_SSID============================Fail')

def set_Guest_WP(driver):
    ##设置访客密码
    w.setWP(driver, guest, pwg)
    w.savewifi(driver, guest)
    if w.getWP(driver, guest, pwg) == 3:
        logging.info('set_Guest_WP=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "setGuestWP-%s.jpg" % test_time)
        logging.warning('set_Guest_WP============================Fail')

def set_Guest_NUll(driver):
    ##访客加密方式为空
    w.setEncryption(driver, guest, 1)
    w.savewifi(driver, guest)
    if w.getEncryption(driver, guest) == 3:
        logging.info('set_Guest_NUll=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "setGuestNUll-%s.jpg" % test_time)
        logging.warning('set_Guest_NUll============================Fail')

def set_Guest_PSK2(driver):
    ##访客加密方式PSK2
    w.setEncryption(driver, guest, 2)
    w.setWP(driver, guest, default_guest)
    w.savewifi(driver, guest)
    if w.getEncryption(driver, guest) == 2:
        logging.info('set_Guest_PSK2=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "setGuestPSK2-%s.jpg" % test_time)
        logging.warning('set_Guest_PSK2============================Fail')

def set_Guest_PSK_PSK2(driver):
    w.setEncryption(driver, guest, 3)
    w.savewifi(driver, guest)
    if w.getEncryption(driver, guest) == 1:
        logging.info('set_Guest_PSK_PSK2=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "setGuestPSK_PSK2-%s.jpg" % test_time)
        logging.warning('set_Guest_PSK_PSK2============================Fail')


def close_Guest_WiFi(driver):
    w.clickWiFi(driver, guest)
    if w.getWiFi(driver, guest) == 3:
        logging.info('close_Guest_WiFi=========================Success')
        return 3
    else:
        driver.get_screenshot_as_file(caseFail + "closeGuestWiFi-%s.jpg" % test_time)
        logging.warning('close_Guest_WiFi============================Fail')


def close_24G_WiFi(driver):
    w.clickWiFi(driver, ra0)
    if w.getWiFi(driver, ra0) == 1:
        logging.info('close_24G_WiFi=========================Success')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "close24WiFi-%s.jpg" % test_time)
        logging.warning('close_24G_WiFi============================Fail')


def close_5G_WiFi(driver):
    w.clickWiFi(driver, rai0)
    if w.getWiFi(driver, rai0) == 2:
        logging.info('close_5G_WiFi=========================Success')
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "close5WiFi-%s.jpg" % test_time)
        logging.warning('close_5G_WiFi============================Fail')

class Test_WiFi:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 1) == 1:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    ###获取2.4G 默认SSID###
    def test_get_Default_24g_SSID(self):
        assert get_Default_24g_SSID(self.driver) == 1

    ###获取 5G 默认SSID###
    def test_get_Default_5g_SSID(self):
        assert get_Default_5g_SSID(self.driver) == 2

    ### 获取2.4G 默认密码 ###
    def test_get_Default_24_Password(self):
        assert get_Default_24g_PW(self.driver) == 1

    ### 获取5G 默认密码###
    def test_get_Default_5g_Password(self):
        assert get_Default_5g_PW(self.driver) == 2

    ### 获取2.4G默认加密类型 ###
    def test_get_Default_24G_Encryption(self):
        assert get_Default_24G_Encryption(self.driver) == 1

    def test_get_Default_5G_Encryption(self):
        assert get_Default_5G_Encryption(self.driver) == 1

    def test_set_24G_SSID(self):
        assert set_24G_SSID(self.driver) == 1

    def test_set_5G_SSID(self):
        assert set_5G_SSID(self.driver) == 2

    def test_set_24G_PW(self):
        assert set_24G_PW(self.driver) == 1

    def test_set_5G_PW(self):
        assert set_5G_PW(self.driver) == 2

    def test_set_24G_Null_PW(self):
        assert set_24G_Null_PW(self.driver) == 3

    def test_set_24G_Psk2_PW(self):
        assert set_24G_Psk2_PW(self.driver) == 2

    def test_set_24G_Psk_Psk2_PW(self):
        assert set_24G_Psk_Psk2_PW(self.driver) == 1

    def test_set_5G_Null_PW(self):
        assert set_5G_Null_PW(self.driver) == 3

    def test_set_5G_Psk2_PW(self):
        assert set_5G_Psk2_PW(self.driver) == 2

    def test_set_5G_Psk_Psk2_PW(self):
        assert set_5G_Psk_Psk2_PW(self.driver) == 1

    def test_get_24G_Hide(self):
        assert get_24G_Hide(self.driver) == 1

    def test_get_5G_Hide(self):
        assert get_5G_Hide(self.driver) == 3

    def test_set_24G_Hide(self):
        assert set_24G_Hide(self.driver) == 2

    def test_set_5G_Hide(self):
        assert set_5G_Hide(self.driver) == 4

    def test_get_Default_24G_HT(self):
        assert get_Default_24G_HT(self.driver) == 1

    def test_get_Default_5G_HT(self):
        assert get_Default_5G_HT(self.driver) == 3

    def test_set_ra0_40_HT(self):
        assert set_ra0_40_HT(self.driver) == 2

    def test_set_ra0_2040_HT(self):
        assert set_ra0_2040_HT(self.driver) == 1

    def test_set_rai0_40_HT(self):
        assert set_rai0_40_HT(self.driver) == 4

    def test_set_rai0_80_HT(self):
        assert set_rai0_80_HT(self.driver) == 5

    def test_set_rai0_2040_HT(self):
        assert set_rai0_2040_HT(self.driver) == 3

    def test_get_Guest(self):
        assert get_Guest(self.driver) == 3

    def test_get_Guest_SSID(self):
        assert get_Guest_SSID(self.driver) == 3

    def test_get_Guest_WP(self):
        assert get_Guest_WP(self.driver) == 3

    def test_get_Guest_Encryption(self):
        assert get_Guest_Encryption(self.driver) == 1

    def test_set_Guest_SSID(self):
        assert set_Guest_SSID(self.driver) == 3

    def test_set_Guest_WP(self):
        assert set_Guest_WP(self.driver) == 3

    def test_set_Guest_NUll(self):
        assert set_Guest_NUll(self.driver) == 3

    def test_set_Guest_PSK2(self):
        assert set_Guest_PSK2(self.driver) == 2

    def test_set_Guest_PSK_PSK2(self):
        assert set_Guest_PSK_PSK2(self.driver) == 1

    def test_close_Guest_WiFi(self):
        assert close_Guest_WiFi(self.driver) == 3

    def test_close_24G_WiFi(self):
        assert close_24G_WiFi(self.driver) == 1

    def test_close_5G_WiFi(self):
        assert close_5G_WiFi(self.driver) == 2



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))