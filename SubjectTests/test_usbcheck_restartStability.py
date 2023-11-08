# -*- coding: utf-8 -*-
import configparser
import logging
import os
import csv
import time
import paramiko
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
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    restart_count = int(config.get('Restart', 'restart_count'))
    cmd = 'reboot'
    logging.info(__file__)
    for i in range(300):
        logging.info(i)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(default_ip, 22, "root", default_pw)
        ssh.exec_command(cmd)
        logging.info('wait time %s' % restart_wtime)
        time.sleep(restart_wtime)
        samba = os.path.exists("S:\\")
        if samba == True:
            logging.info("open Smaba success")
        else:
            logging.error("open Smaba fail")
            pytest.fail('Open Samba fail')
            break

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))