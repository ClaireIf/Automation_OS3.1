# -*- coding:utf-8 -*-

import configparser
import logging
import os
import time
import pytest
import paramiko
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.advanced_setup
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.advanced_setup import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
ads = advanced_setup()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
t.get_test_ip()
logging.info(__file__)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
default_dmzip = config.get('Default', 'default_dmz')
dmz_ip = config.get('DMZ', 'dmz_ip')
dmzip1 = config.get('DMZ', 'dmzip1')


def default_dmz_status(self):
    return ads.getDMZ(self)

def open_dmz(self):
    if ads.clickDMZ(self)== 1:
        if ads.getDMZ(self) == 2:
            return ads.getDMZStatus(self)

def default_DMZ_IP(self):
    if ads.getDMZ(self)==1:
        ads.clickDMZ(self)
    return ads.getDMZIP(self, dmz_ip, default_dmzip)

def set_dmz_ip(self):
    if ads.getDMZ(self)==1:
        ads.clickDMZ(self)
    if ads.setDMZ(self, dmz_ip) == 1:
        if ads.saveDMZ(self) == 1:
            return ads.getDMZIP(self, dmz_ip, default_dmzip)

def ssh_cmd():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22, "root", default_pw)
    stdin, stdout, stderr = ssh.exec_command("uci show firewall")
    list = stdout.readlines()
    logging.info(list)
    ssh.close()
    x = 0
    for dmz_result in list:
        dmz_result1 = str.split(dmz_result)[0]
        logging.info(dmz_result1)
        if dmz_result1 =="firewall.@dmz[0].switch='1'":
            x = 1
            break
        else:
            continue
    for dmz_result in list:
        dmz_result1 = str.split(dmz_result)[0]
        if dmz_result1 == "firewall.@dmz[0].enabled='0'":
            x = 2
            break
        else:
            for dmz_result in list:
                dmz_result1 = str.split(dmz_result)[0]
                if dmz_result1 == ("firewall.@dmz[0].dest_ip='%s'" % str(dmzip1 + default_dmzip)):
                    x = 3
                    continue
                elif dmz_result1 == ("firewall.@dmz[0].dest_ip='%s'" % str(dmzip1 + dmz_ip)):
                    x = 4
                    continue
    logging.info(x)
    return x


class TestDMZ:
    def setup_class(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if ads.adsetupChoose(self.driver) == 1:
                    ads.PortDMZ(self.driver)

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_default_dmz_status(self):
        assert default_dmz_status(self.driver) == 1

    def test_open_dmz(self):
        assert open_dmz(self.driver) == 2

    def test_default_DMZ_IP(self):
        assert default_DMZ_IP(self.driver) == 2

    def test_set_dmz_ip(self):
        assert set_dmz_ip(self.driver) == 1

    def test_check_dmz_ssh(self):
        assert ssh_cmd() == 4


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))