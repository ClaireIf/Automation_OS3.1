# -*- coding:utf-8 -*-
###################################
#   升级
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
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

def case(build):
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
    new_build = build
    new_version = config.get('Upgrade', 'old_version')
    upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
    cmd = 'cat /etc/openwrt_version'
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 5) == 5:
                if rs.upgrade(driver, new_build, upgrade_wtime) == 1:
                    driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
                    driver.quit()
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(default_ip, 22, "root", default_pw)
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    ssh_version = str.strip(stdout.readlines()[0])
                    logging.info(ssh_version)
                    logging.info('new_version = %s ,ssh_version =%s' % (new_version, ssh_version))
                    if ssh_version == new_version:
                        logging.info(filename + "success")
                        return 1
                    else:
                        return 0
    driver.quit()


def test_oldBuild():
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    build = config.get('Upgrade', 'old_build')
    assert case(build) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))