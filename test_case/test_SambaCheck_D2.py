# -*- coding: utf-8 -*-

import configparser
import logging
import csv
import os
import pytest
import shutil
#########################
#  import module
#########################
import sys
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
import modules.router_status
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from modules.router_status import *
from tools import *
#########################
from selenium import webdriver


def case(sChoose):
    if sChoose == 1:
        path_128='S:\\'
        files = os.listdir(path_128)
        print(files)
        for file in files:
            print(file)
            if file == '.128M.ext4.iso':
                return 1
    if sChoose == 2:
        path_xcloud='S:\\xcloud'
        copyfile = os.path.dirname(os.getcwd())+"/upfile/test.bin"
        files = os.listdir(path_xcloud)
        result = 0
        for file in files:
            print(file)
            test_xcloudpath = path_xcloud + '\\' + file
            if file == 'music':
                shutil.copy(copyfile, test_xcloudpath)
            if file =='video':
                shutil.copy(copyfile, test_xcloudpath)
            if file =='docs':
                shutil.copy(copyfile, test_xcloudpath)
            if file =='pic':
                shutil.copy(copyfile, test_xcloudpath)
            binfiles = os.listdir(test_xcloudpath)
            for binfile in binfiles:
                if binfile == 'test.bin':
                    result = result + 1
                    os.remove(test_xcloudpath+'/test.bin')
                    print(result)
        if result == 4:
            return 1


def test_check_128iso():
    assert case(1) == 1

def test_xcloudfile():
    assert case(2) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))