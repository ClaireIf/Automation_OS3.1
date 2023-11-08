# -*- coding: utf-8 -*-

import time
import paramiko
import logging
import os
import pytest
import shutil


def test_do():
    for i in range(500):
        print('=============== Run test ==============%s' % i)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.99.1', 22, "root", '12345678')
        ssh.exec_command('wifi')
        time.sleep(10)
        print('>>>>>>>>>>>>>>>>>>>>')
        ssid_cmd = ['iwconfig ra0', 'iwconfig rai0']
        #print(ssid_cmd)
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