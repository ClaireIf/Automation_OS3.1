# -* coding:utf-8 -*-
###################################
#  完成初始化配置，浏览器打开网页
###################################

import logging
import os
import time
import pytest

import sys
import conftest
sys.path.append("..") #引用modules模块
import modules.login_router
import modules.initialize
from modules.login_router import *
from modules.initialize import *
from tools import *
###################################
from selenium import webdriver

def openUrl():
    val = login_router()
    t = tools()
    hp = initialize()
    filename=os.path.basename (__file__).split('.')[0]
    t.log(filename)
    logging.info(__file__)
    test_url = ['ok.go/','xyun.co','newifi.com','wi.fi']
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    num1 = 0
    for i in test_url:
        if val.open_url(driver,'http://'+i)==1:
            num1=num1+1
            if num1 == 4:
                return 1
            else:
                return 2
        if val.open_url(driver,'http://'+i) ==2:
            num1 =num1+1
            if num1 == 4:
                return 3
            else:
                return 4

    driver.quit()

def test_domainJumpLogin():
    assert openUrl() == 1

def test_domainJumpInitialize():
    assert openUrl() == 3
    
if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))



