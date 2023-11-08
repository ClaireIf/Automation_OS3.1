# -*- coding:utf-8 -*-
###################################
#   互联网设置静态IP
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import paramiko
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
pppoe_user = config.get('PPPOE', 'pppoe_user')
pppoe_pw = config.get('PPPOE', 'pppoe_pw')
mtu = config.get('PPPOE', 'mtu')
pppoe_dns = config.get('PPPOE', 'pppoe_dns')
new_build = config.get('Upgrade', 'new_build')
upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
restart_wtime = int(config.get('Restart', 'restart_wtime'))
logging.info(__file__)

# def setPPPoE(self):
#     if rs.setup_choose(self, 2) == 2:
#         time.sleep(2)
#         if rs.setPPPoE(self, 0, pppoe_user, pppoe_pw, mtu, pppoe_dns) == 1:
#             return 1

def restart(self):
    if rs.setup_choose(self, 5) == 5:
        if rs.restart(self, restart_wtime) == 1:
            return 1

def update(self):
    if rs.setup_choose(self, 5) == 5:
        if rs.upgrade(self, new_build, upgrade_wtime) == 1:
            return 1

def getPPPoE(self):
    if rs.setup_choose(self, 2) == 2:
        time.sleep(2)
        if rs.get_pppoes(self, pppoe_user, pppoe_pw, mtu, pppoe_dns) == 4:
            return 4

class TestPPPoE:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://'+default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                pass

    def teatdown(self):
        self.driver.close()
        self.driver.quit()

    # def test_setPPPoE(self):
    #     assert setPPPoE(self.driver) == 1

    def test_update(self):
        assert update(self.driver) == 1

    def test_getPPPoE_update(self):
        assert getPPPoE(self.driver) == 4

    def test_restart(self):
        assert restart(self.driver) == 1

    def test_getPPPoE_restart(self):
        assert getPPPoE(self.driver) == 4


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))