# -*- coding: utf-8 -*-
###################################
#   升级
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import shutil
import pytest
import conftest
#########################
#  import module
#########################
import sys
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
filename = os.path.basename(__file__).split('.')[0]
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
new_build = config.get('Upgrade', 'new_build')
upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))



def Upgrade(self):
    if rs.setup_choose(self, 5) == 5:
        if rs.upgrade(self, new_build, upgrade_wtime) == 1:
            return 1


class Test_Auto_Upgrade:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://'+default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_auto_upgrade(self):
        print(u'自动化升级')
        assert Upgrade(self.driver) ==1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))