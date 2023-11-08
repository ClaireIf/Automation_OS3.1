# -*- coding: utf-8 -*-

import time
import paramiko
import logging
import configparser
import os
import pytest
import sys
sys.path.append("..")
from tools import *


def test_do():
    t = tools()
    filename = os.path.basename(__file__).split('.')[0]
    projectpath = os.path.diraname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default','default_ip')
    default_pw = config.get('Default','default_pw')
    config.read(config_file)
    for i in range(1000):
        print('=============== Run test ==============%s' % i)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(default_ip, 22, "root", default_pw)
        ssh.exec_command('ifconfig eth0.2 down')
        time.sleep(30)
        ssh.exec_command('ifconfig eth0.2 up')
        time.sleep(180)
        if t.urlRequest('www.baidu.com') == 1:
            logging.info('ping OK')
        else:
            break
            logging.info('ping baidu fail>>>>>>>>')
            pytest.fail('fail')


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
