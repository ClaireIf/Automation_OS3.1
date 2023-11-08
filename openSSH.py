# -*- coding: utf-8 -*-

import time
from selenium import webdriver

def open_SSH():
    default_ip = "192.168.99.1"
    driver = webdriver.Chrome()
    driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
    time.sleep(3)
    driver.close()
    driver.quit()


open_SSH()
