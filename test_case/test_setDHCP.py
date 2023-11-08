# -*- coding:utf-8 -*-
###################################
#   互联网获取wifi配置
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import csv
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
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    cmd = "sed -i '$d' /tmp/resolv.conf.auto"
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    #访问管理页面
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        # 输入密码登录
        if lr.login(driver, default_pw) == 1:
            # 切换到互联网设置页面
            if rs.setup_choose(driver, 2) == 2:
                time.sleep(2)
            else:
                logging.warning("===test fail setup choose===")
            rs.setDHCP(driver)
            t.ssh_cmd(default_ip, default_pw, cmd)
            result = t.ping("www.baidu.com")
            if result == 0:
                logging.info("==set DNS success")
                logging.info("Auto13 success")
                return 1
                driver.close()
            else:
                logging.error("===set DNS fail===")
                return 0
                driver.close()
        else:
            logging.warning("===test fail login===")
            return 0
            driver.close()
    else:
        logging.warning("===test fail open url===")
        return 0
        driver.close()


def test_do():
    assert case() == 1


if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))