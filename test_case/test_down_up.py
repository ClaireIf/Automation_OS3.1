# -*- coding: utf-8 -*-

import os
import time
import pytest
import paramiko
import logging
import configparser
import sys
import conftest
sys.path.append("..")
from tools import *
#########################
from selenium import webdriver

t = tools()
filename = os.path.basename(__file__).split('.')[0]
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
for i in range(300):
    os.system('test_downgrade.py')
    time.sleep(420)
    os.system('test_reset.py')
    time.sleep(180)
    os.system('test_setupD1DHCPNew.py')
    time.sleep(120)
    os.system('test_update.py')
    time.sleep(420)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
    time.sleep(1)
    driver.close()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22, "root", default_pw)
    ssid_cmd = ['iwconfig ra0', 'iwconfig rai0']
    print(ssid_cmd)
    for ssid_cmd in ssid_cmd:
        stdin, stdout, stderr = ssh.exec_command(ssid_cmd)
        lists = str.strip(stdout.readlines()[1])
        logging.info(lists)
        if lists == 'Link Quality:0  Signal level:0  Noise level:0':
            logging.info('restart wifi close')
            pytest.fail('restart wifi close')
            break
        else:
            logging.info('restart wifi open')

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))