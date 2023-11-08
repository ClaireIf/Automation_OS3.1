# -*- coding: utf-8 -*-
import os
import time
import logging
import configparser
import pytest
import sys
sys.path.append("..")
from tools import *

def test_connwifi():
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    # default_ip ='www.baidu.com'
    path = 'E:\\git\\OS3.1\\RatToolAgent\\'
    fail2 = 0
    fail5 = 0
    for i in range(500):
        logging.info('=====RUN TEST =====%s' % i)
        os.popen(path + "wlanman.exe conn 1c208e04-4dcc-4809-baad-541b0ab8aa3b newifi_58bb i newifi_58bb 20:76:93:3e:58:ba")
        time.sleep(15)
        if t.urlRequest(default_ip) == 1:
            logging.info('2.4G WiFi Conn OK ')
            os.popen(path+ 'wlanman.exe dc 1c208e04-4dcc-4809-baad-541b0ab8aa3b')
        else:
            fail2 = fail2 + 1
            logging.error('2.4G Fail')
        time.sleep(15)
        os.popen(path+ 'wlanman.exe conn 1c208e04-4dcc-4809-baad-541b0ab8aa3b newifi_58bb_5G i newifi_58bb_5G 20:76:93:3e:58:bc')
        time.sleep(15)
        if t.urlRequest(default_ip) == 1:
            logging.info('5G WiFi Conn OK')
            os.popen(path+ 'wlanman.exe dc 1c208e04-4dcc-4809-baad-541b0ab8aa3b')
        else:
            fail5 = fail5 + 1
            logging.error('5G Fail')
        time.sleep(15)
    logging.info('=================Fail 2.4G Count =============%s' % fail2)
    logging.info('=================Fail 5G Count =============%s' % fail5)

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))