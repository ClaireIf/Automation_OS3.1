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
from modules.download_APP import *
from tools import *

LA = login_APP()
DL = download_APP()
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
TestPW = config.get('Password','TestPW')
link = config.get('downlink', 'link')

logging.info(__file__)

def addDown_link_cancel(app):
    if DL.addDown_link(app, '', 2) == 2:
        return 2

def addDown_link_sure(app):
    if DL.addDown_link(app, link, 1) == 1:
        return 1



class Test_download_link:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)
        if DL.click_download(self.app) == 1:
            if DL.click_addDown(self.app) == 1:
                pass

    def teardown(self):
        LA.closed(self.app)

    def test_addDown_link_canel(self):
        assert addDown_link_cancel(self.app) == 2

    def test_addDown_link_sure(self):
        assert addDown_link_sure(self.app) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


