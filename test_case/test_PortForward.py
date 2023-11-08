#-*- coding:UTF-8 -*-

#########################
#       端口转发        #
#########################

from selenium import webdriver
import sys
import time,os
import pytest
import configparser
import conftest
sys.path.append("..")
############################
#       导入自定义模块     #
############################
from modules.login_router import *
from modules.advanced_setup import *



portforward_test = advanced_setup()

path = os.path.dirname(os.getcwd())
config = configparser.ConfigParser()
config.read(path+"/configure/testconfig.ini",encoding='UTF-8')
default_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_passward")
#读取参数配置
name = config.get("Port_Forward","autoname")
section_TCP = config.get("Port_Forward","portSection_TCP")
section_UDP = config.get("Port_Forward","portSection_UDP")
section_TCP_UDP = config.get("Port_Forward","portSection_TCP_UDP")
ip = config.get("DMZ","dmz_ip")
out_port = config.get("Port_Forward","portforward_outport")
in_port = config.get("Port_Forward","portforward_inport")
state_y = config.get("Port_Forward","state_y")
state_n = config.get("Port_Forward","state_n")
action_save = config.get("Port_Forward","action_save")
action_cancel = config.get("Port_Forward","action_cancel")
full_ip = config.get("DMZ","dmzip1")
delete_sure = config.get("Port_Forward","delete_sure")
delete_cancel = config.get("Port_Forward","delete_cancel")

#保存新条目
def save_portforward(driver,portSection_port_name,portSection,last_ip,outport,inport,state,action):
    if portforward_test.click_newbutton(driver) == 1:
        if  portforward_test.set_newportfoward(driver,portSection_port_name,portSection,last_ip,outport,inport,state) == 1:
            return portforward_test.save_cancel_portforward(driver,action)
#检查保存的规则
def check_portforward(driver,portSection_port_name,portSection,last_ip,outport,inport,state,fullip):
    return portforward_test.checkportforward(driver,portSection_port_name,portSection,last_ip,outport,inport,state,fullip)

#取消删除规则
def not_deleteportforward(driver,operation,portSection_port_name,portSection,last_ip,outport,inport,state,fullip):
        if portforward_test.delete_portforward(driver,operation) == 1:
            return portforward_test.checkportforward(driver,portSection_port_name,portSection,last_ip,outport,inport,state,fullip)
#删除规则
def deleteportforward(driver,operation):
    if portforward_test.delete_portforward(driver,operation) == 1:
        return portforward_test.check_no_portforward(driver)


#取消保存设置的规则
def cancelsave_portforward(driver,portSection_port_name,portSection,last_ip,outport,inport,state,action):
    if portforward_test.click_newbutton(driver) == 1:
        if portforward_test.set_newportfoward(driver,portSection_port_name,portSection,last_ip,outport,inport,state) == 1:
            if portforward_test.save_cancel_portforward(driver,action) == 1:
                return portforward_test.check_no_portforward(driver)


class TestPortFoward:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
       # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        auto = login_router()
        auto.open_url(self.driver,'http://'+default_ip)
        auto.login(self.driver,pwd)
        time.sleep(5)
        openadsetup = advanced_setup()
        openadsetup.adsetupChoose(self.driver)
        time.sleep(3)
    def teardown(self):
        self.driver.quit()
    def test_save_portforward(self):
        assert save_portforward(self.driver,name,section_TCP,ip,out_port,in_port,state_y,action_save) == 1
    def test_check_portforward(self):
        assert check_portforward(self.driver,name,section_TCP,ip,out_port,in_port,state_y,full_ip) == 1
    def test_notdeleteportforward(self):
        assert not_deleteportforward(self.driver,delete_cancel,name,section_TCP,ip,out_port,in_port,state_y,full_ip) == 1
    def test_delete_portforward(self):
        assert deleteportforward(self.driver,delete_sure) == 1
    def test_cancelsave_portforward(self):
        assert cancelsave_portforward(self.driver,name,section_TCP,ip,out_port,in_port,state_y,action_cancel) == 1

if __name__=='__main__':
    pytest.main(os.path.basename(__file__))