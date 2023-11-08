# -*- coding:utf-8 -*-
###################################
#  测试重启时WiFi启动
###################################
import configparser
import logging
import os
import time
import pytest
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


def test_do():
    lr = login_router()
    rs = router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    restart_count = int(config.get('Restart', 'restart_count'))
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    for i in range(restart_count):
        logging.info('===run test=== %s', i+1)
        fail = 0
        t.ssh_cmd(default_ip, default_pw, 'reboot', 2)
        time.sleep(restart_wtime)
        if t.urlRequest('www.baidu.com') == 1:
            logging.info("restart Stability success")
        else:
            logging.error("restart Stability fail")
            fail = fail + 1
            logging.info("fail count ======== %s", fail)
            break


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
