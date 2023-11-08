import time,os,logging,configparser,pytest
from appium import webdriver
import conftest
import sys
sys.path.append("..")
import modules.login_APP
import modules.setup_APP
import modules.login_router
from modules.login_router import *
from modules.login_APP import *
from modules.setup_APP import *
from tools import *

LA = login_APP()
ST = setup_APP()
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
account = 'claire.x@outlook.com'
pw = 'zyx7280'

logging.info(__file__)

def setup_login(app):
    if LA.enter_login(app) ==1:
        if LA.login(app, account, pw) ==1:
            return 1

class Test_setup_swipe:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)

    def teardown(self):
        LA.closed(self.app)

    def test_setup_swipe(self):
        assert setup_login(self.app) == 1



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))