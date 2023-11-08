# -*- coding:utf-8 -*-
###################################
#  测试重启时WiFi启动
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
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from modules.wifi import *
from tools import *
#########################
from selenium import webdriver


def test_do():
    lr = login_router()
    rs = router_setup()
    w = wifi()
    t = tools()
    ra0 = 1
    rai0 = 2
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    restart_count = int(config.get('Restart', 'restart_count'))
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    for i in range(restart_count):
        driver = webdriver.Chrome()
        driver.maximize_window()
        fail = 0
        logging.info('TEST COUNT = %s ' % i)
        if lr.open_url(driver, 'http://'+default_ip) == 1:
            if lr.login(driver, default_pw) == 1:
                rs.setup_choose(driver, 1)
                for x in range(2):
                    w.clickWiFi(driver, ra0)
                    time.sleep(10)
                    w.clickWiFi(driver, rai0)
                    time.sleep(20)
                driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
                time.sleep(1)
                driver.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(default_ip, 22, "root", default_pw)
                ssid_cmd = ['iwconfig ra0', 'iwconfig rai0']
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
            else:
                fail = fail + 1
                logging.warning("===test fail===")
                logging.info("fail count ======== %s", fail)
                driver.close()
                continue
        else:
            fail = fail + 1
            logging.warning("===test fail===")
            logging.info("fail count ======== %s", fail)
            driver.close()
            continue




if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))