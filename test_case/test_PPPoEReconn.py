# -*- coding: utf-8 -*-
###################################
#   PPPOE重连
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


def case():
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
    pppoe_pw = config.get('PPPOE','pppoe_pw' )
    mtu = config.get('PPPOE','mtu')
    pppoe_dns = config.get('PPPOE','pppoe_dns')
    cmd1 = 'ifdown wan'
    cmd2 = 'ifup wan'
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 2) == 2:
                time.sleep(2)
                if rs.setPPPoE(driver, 0, pppoe_user, pppoe_pw, mtu, pppoe_dns) == 1:
                    t.ssh_cmd(default_ip, default_pw, cmd1, 2)
                    time.sleep(60)
                    t.ssh_cmd(default_ip, default_pw, cmd2, 2)
                    time.sleep(180)
                    if t.ping('www.baidu.com') ==0:
                        return 1
    driver.quit()

def test_PPPoEReconn():
    assert case() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))