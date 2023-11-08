# -*- coding:utf-8 -*-
###################################
#  测试重启时WiFi启动
###################################
import configparser
import logging
import os
import pytest
import paramiko
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
fail = 0


def check_url():
    #######检查网络######
    if t.urlRequest('www.baidu.com') == 1:
        logging.info("restart Stability success")
    else:
        logging.error("restart Stability fail")

def check_wifi():
    ##########检查wifi启动#######
    ssid_cmd = ['iwconfig ra0', 'iwconfig rai0']
    for ssid_cmd in ssid_cmd:
        lists = str.strip(t.ssh_cmdss(default_ip,default_pw,ssid_cmd)[1])
        logging.info(lists)
        if lists == 'Link Quality:0  Signal level:0  Noise level:0':
            logging.info('restart wifi close')
        else:
            logging.error('restart wifi open')

def check_usb():
    samba = os.path.exists("S:\\")
    if samba == True:
        logging.info("open Smaba success")
    else:
        logging.error("open Smaba fail")

def check_progress():
    cmds = ["ps | grep xCloudClient", "ps | grep xcloud_manager", "ps |grep smbd", "ps |grep minidlna","ps |grep miniupnpd","ps |grep pic",]
    for cmd in cmds:
        list = t.ssh_cmdss(default_ip, default_pw, cmd)
        for result in list:
            logging.info("==============================")
            logging.info(result)
            get_course_type = str.split(result)[3]
            get_course = str.split(result)[4]
            if get_course_type == 'S':
                if get_course == "/usr/local/xcloud/bin/xCloudClient":
                    logging.info("xCloudClient ====== OK")
                if get_course == "/usr/sbin/xcloud_manager":
                    logging.info("xcloud_manager ======= OK")
                if get_course == "/usr/sbin/smbd":
                    logging.info("smbd ======= OK")
                if get_course == "/usr/bin/minidlna":
                    logging.info("minidlna ======== OK")
                if get_course == "/usr/sbin/miniupnpd":
                    logging.info("miniupnpd ======= OK")
                if get_course == "/sbin/pic_backup":
                    logging.info('pic_backup====OK')
            elif get_course_type == 'R':
                pass
            else:
                logging.error("%s ============ Fail" % cmd)


class Test_Restart_Stabilitys:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://'+default_ip+'/newifi/ifiwen_hss.html')
        if lr.open_url(self.driver, 'http://'+default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 5):
                    if rs.restart(self.driver, restart_wtime):
                        pass


    def teardown(self):
        self.driver.close()
        self.driver.quit()


    def test_restart(self):
        check_url()
        check_wifi()
        check_usb()
        check_progress()





if __name__ == '__main__':
    for i in range(restart_count):
        logging.info('====Run test====%s' %i)
        pytest.main(os.path.basename(__file__))
