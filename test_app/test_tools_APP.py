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
pw = 12345678
Name ="迅雷远程下载"
logging.info(__file__)

def tools_install(app):
    if SET.tools_online(app) ==1:
        if SET.tools_install(app) ==1:
            if SET.tools_installed(app) == 1:
                if SET.tools_getInstalled(app) ==1:
                    return 1

def tools_uninstall_cancel(app):
    if SET.tools_installed(app) ==1:
        if SET.tools_uninstall(app,2) ==2:
            if SET.tools_getInstalled(app) ==1:
                return 1

def tools_uninstall_sure(app):
    if SET.tools_installed(app) ==1:
        if SET.tools_uninstall(app,1) ==1:
            if SET.tools_getInstalled(app) ==0:
                return 1

class Test_tools:
    def setup(self):
        self.app = LA.startApp(platformVersion, deviceName)
        if SET.set_app(self.app) == 1:
            if SET.tools_click(self.app) == 1:
                pass

    def teardown(self):
        LA.closed(self.app)

    def test_tools_install(self):
        assert tools_install(self.app) ==1

    def test_tools_uninstall_cancel(self):
        assert tools_uninstall_cancel(self.app) ==1

    def test_tools_uninstall_sure(self):
        assert tools_uninstall_sure(self.app) ==1



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))