# -*- coding: utf-8 -*-
import configparser
import os
import paramiko
import pytest
import time
from selenium import webdriver
import conftest

def hosts():
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    cmd ='cat /etc/hosts'
    result = 0
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    time.sleep(1)
    driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
    driver.quit()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22, "root", default_pw)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    hosts = stdout.readlines()
    ssh.close()
    print(hosts)
    if str.strip(hosts[0]) == '127.0.0.1 localhost':
        result = result + 1
    if str.strip(hosts[1]) == '192.168.99.1 xyun.co':
        result = result + 1
    if str.strip(hosts[2]) == '192.168.99.1 ok.go':
        result = result + 1
    if str.strip(hosts[3]) == '192.168.99.1 wi.fi':
        result = result + 1
    if str.strip(hosts[4]) == '192.168.99.1 newifi.com':
        result = result + 1
        return result


def test_hosts():
    assert hosts() == 5


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))