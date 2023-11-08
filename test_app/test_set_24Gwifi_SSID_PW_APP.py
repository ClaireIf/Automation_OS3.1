import time,os,logging,configparser,pytest
from appium import webdriver
import sys
sys.path.append("..")
import modules.login_APP
import modules.set_APP
from modules.login_APP import *
from modules.set_APP import *
from tools import *

LA = login_APP()
SET = set_APP()
t = tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig_APP.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
platformVersion = config.get('Devices', 'version')
deviceName = config.get('Devices', 'deviceName')
SSID_24G = config.get('WiFi', 'SSID_24G')
wifi_PW_24G = config.get('WiFi', 'wifi_PW')
logging.info(__file__)

def cancel_set_24Gwifi_SSID_PW_24G(app):
    if SET.set_app(app) ==1:
        if SET.click_wifi(app) ==1:
            if  SET.set_24Gwifi_SSID_PW(app, SSID_24G, wifi_PW_24G, 2) == 2:
                return 2

def set_24Gwifi_SSID_PW_24G(app):
    if SET.set_app(app) == 1:
        if SET.click_wifi(app) == 1:
            if  SET.set_24Gwifi_SSID_PW(app, SSID_24G, wifi_PW_24G, 1) == 1:
                return 1


class Test_retart:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)

    def teardown(self):
        LA.closed(self.app)

    def test_cancel_set_24Gwifi_SSID_PW_24G(self):
        assert cancel_set_24Gwifi_SSID_PW_24G(self.app) ==2

    def test_set_24Gwifi_SSID_PW_24G(self):
        assert set_24Gwifi_SSID_PW_24G(self.app) ==1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))