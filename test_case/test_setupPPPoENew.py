# -*- coding: utf-8 -*-
###################
##新版初始化-PPPoE
###################

import configparser
import logging
import os
import csv
import pytest
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.initialize_new import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
setup = initialize()
t = tools()
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
pppoe_user = config.get('PPPOE', 'pppoe_user')
pppoe_pw = config.get('PPPOE', 'pppoe_pw')
logging.info(__file__)



def pppoe_conn(self):
    if setup.homepage(self) == 1:
        if setup.detection_pppoe(self, pppoe_user, pppoe_pw):
            if setup.initialize_pw(self, default_pw) == 1:
                if setup.complete(self) == 1:
                    return 1

class TestPPPoE:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://'+default_ip) == 2:
            pass

    def test_PPPoE_Conn(self):
        assert pppoe_conn(self.driver) == 1

    def teardown(self):
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))