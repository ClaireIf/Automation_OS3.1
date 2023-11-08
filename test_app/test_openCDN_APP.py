import time,os,logging,configparser,pytest
from appium import webdriver
import sys
sys.path.append("..")
import modules.login_APP
import modules.homepage_APP
from modules.login_APP import *
from modules.homepage_APP import *
from tools import *

LA = login_APP()
HM = homepage_APP()
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


def cancelCDN(app):
    if HM.clickCDN(app) ==1:
        if HM.cancelCDN(app) ==1:
            return 1

def openCDN(app):
    if HM.clickCDN(app) ==1:
        if HM.openCDN(app) ==1:
            return 1



class Test_retart:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)

    def teardown(self):
        LA.closed(self.app)

    def test_cancelCDN(self):
        assert cancelCDN(self.app) == 1

    def test_openCDN(self):
        assert openCDN(self.app) == 1



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))