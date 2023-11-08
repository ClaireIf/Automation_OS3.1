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
logging.info(__file__)

def cancel_encryption_WPA2_wifi_5G(app):
    if SET.set_5Gwifi_encryption(app, 1, 2) == 2:
        return 2

def encryption_WPA2_wifi_5G(app):
    if SET.set_5Gwifi_encryption(app, 1, 1) == 1:
        return 1

def cancel_encryption_WAP_WPA2_wifi_5G(app):
    if SET.set_5Gwifi_encryption(app, 2, 2) == 2:
        return 2

def encryption_WAP_WPA2_wifi_5G(app):
    if SET.set_5Gwifi_encryption(app, 2, 1) == 1:
        return 1

def cancel_encryption_NULL_wifi_5G(app):
    if SET.set_5Gwifi_encryption(app, 3, 2) == 2:
        return 2

def encryption_NULL_wifi_5G(app):
    if SET.set_5Gwifi_encryption(app, 3, 1) == 1:
        return 1

class Test_retart:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)
        if SET.set_app(self.app) == 1:
            if SET.click_wifi(self.app) == 1:
                pass

    def teardown(self):
        LA.closed(self.app)

    def test_cancel_encryption_WPA2_wifi_5G(self):
        assert cancel_encryption_WPA2_wifi_5G(self.app) == 2

    def encryption_WPA2_wifi_5G(self):
        assert encryption_WPA2_wifi_5G(self.app) == 1

    def test_cancel_encryption_WAP_WPA2_wifi_5G(self):
        assert cancel_encryption_WAP_WPA2_wifi_5G(self.app) == 2

    def test_encryption_WAP_WPA2_wifi_5G(self):
        assert encryption_WAP_WPA2_wifi_5G(self.app) == 1

    def test_cancel_encryption_NULL_wifi_5G(self):
        assert cancel_encryption_NULL_wifi_5G(self.app) == 2

    def encryption_NULL_wifi_5G(self):
        assert encryption_NULL_wifi_5G(self.app) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))