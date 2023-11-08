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
onePW = config.get('Password', 'onePW')
surePW = config.get('Password', 'surePW')
TestPW = config.get('Password','TestPW')
logging.info(__file__)


def change_Router_Password_Cancel(app):

        if SET.set_AdminPW(app,onePW,surePW,2) ==2:
            return 1

def change_Router_Password_Sure(app):
        if SET.set_AdminPW(app,onePW,surePW,1) ==1:
            return 1


def change_Router_TestPassword_Sure(app):
    if SET.set_AdminPW(app, TestPW, TestPW, 1) == 1:
        return 1

class Test_retart:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)
        if SET.set_app(self.app) ==1:
            if SET.changeAdminPW(self.app) == 1:
                pass

    def teardown(self):
        LA.closed(self.app)

    def test_change_Router_Password_Cancel(self):
        assert change_Router_Password_Cancel(self.app) == 1

    def test_change_Router_Password_Sure(self):
        assert change_Router_Password_Sure(self.app) == 1

    def test_change_Router_TestPassword_Sure(self):
        assert change_Router_TestPassword_Sure(self.app) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))