# -*- coding:utf-8 -*-
###################################
#   测试登录
###################################

import logging
import os
import time
import pytest
import sys
sys.path.append("..")
from tools import *
from selenium import webdriver

t =tools()
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)

def test_case():
    fail = 0
    for i in range(1000):
        try:
            logging.info("=====Test Count ====%s" % i)
            driver = webdriver.Chrome()
            t.urlRequest('www.baidu.com')
            driver.get("http://sc.sina.com.cn")
            # time.sleep(10)
            try:
                driver.find_element_by_xpath("//*[@id='header']/div[1]/h2").is_displayed()
                logging.info("=========open success=======")
            except:
                driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/openBaidu_Stability-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                fail = fail + 1
                logging.info("=========Fail =======%s" % fail)
            driver.close()
            driver.quit()
        except:
            t.urlRequest('www.baidu.com')
            driver.close()
            driver.quit()




if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))