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
from modules.account_APP import *
from tools import *

LA = login_APP()
ACC = account_APP()
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

def unbind_cancel(app):
    if ACC.unbinding(app,2) == 2:
        return 2

def unbind_sure(app):
    if ACC.unbinding(app,1) ==1:
        return 1

class Test_unbind:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)
        if ACC.click_account(self.app) == 1:
            pass

    def teardown(self):
        LA.closed(self.app)

    def test_unbind_canel(self):
        assert unbind_cancel(self.app) == 2

    def test_unbind_sure(self):
        assert unbind_sure(self.app) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))