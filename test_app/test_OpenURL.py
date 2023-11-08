# -* coding:utf-8 -*-
###################################
#  完成初始化配置，浏览器打开网页
###################################
import logging,configparser
import os
import time
import pytest

import sys
import conftest
sys.path.append("..")  # 引用modules模块
import modules.login_router
import modules.initialize
from modules.login_router import *
from modules.initialize import *
from tools import *
###################################
from selenium import webdriver


def OpenUrl():
    lr = login_router()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = projectpath + '/errorpng/caseFail/'
    test_time =time.strftime("%Y%m%d%H%M%S",time.localtime())
    filename = os.path.basename(__file__).split('.')[0]
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    t.log(filename)
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    # driver = webdriver.Chrome()
    if lr.open_url(driver, 'http://' + default_ip) == 2:
        logging.info('===========================Successs')
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "OpenURL-%s.jpg" % test_time)
        logging.info('============================Fail')
    driver.close()
    driver.quit()


def test_OpenUrl():
    assert OpenUrl() == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))



