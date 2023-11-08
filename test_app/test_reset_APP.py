import time,os,logging,configparser,pytest
from appium import webdriver
import conftest
import sys
sys.path.append("..")
import modules.login_APP
import modules.set_APP
import modules.login_router
from modules.login_router import *
from modules.login_APP import *
from modules.set_APP import *
from tools import *

LA = login_APP()
SET = set_APP()
lr = login_router()
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

def reset_cancel(app):
    if SET.set_app(app) ==1:
        if  SET.reset_app(app,2) ==2:
            return 2

def reset_sure(app):
    if SET.set_app(app) ==1:
        if  SET.reset_app(app,1) ==1:
            return 1


class Test_retart:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)

    def teardown(self):
        LA.closed(self.app)

    def test_restart_cancel(self):
        assert reset_cancel(self.app) ==2

    def test_restart_sure(self):
        assert reset_sure(self.app) ==1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))