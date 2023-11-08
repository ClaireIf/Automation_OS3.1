# -*- coding: utf-8 -*-
import os
import time
import logging
import sys
import pytest
sys.path.append("..")
from tools import *
from selenium import webdriver

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test_xiaoyun.log',
                    filemode='a')
#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

def test_upfiles():
    uppath = 'E:\\xDownload2\\'
    ip = '192.168.99.1'
    logging.info(__file__)
    files = os.listdir(uppath)
    files.sort(key=lambda x: int(x[:-8]))
    # print(files)
    logging.info(files)
    i = 0
    while i < 1000:
        driver = webdriver.Chrome()
        for upfile in files[i:i+5]:
            print(upfile)
            logging.info(upfile)
            driver.get('http://' + ip + ':9091/transmission/web/')
            logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Star')
            driver.find_element_by_id('toolbar-open').click()
            time.sleep(3)
            logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>UPfile')
            driver.find_element_by_id('torrent_upload_file').send_keys(uppath + upfile)
            time.sleep(3)
            driver.find_element_by_id('upload_confirm_button').click()
            time.sleep(3)
        i = i + 5
        logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END')
        time.sleep(10)
        driver.find_element_by_id("toolbar-pause-all").click()
        driver.close()


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))