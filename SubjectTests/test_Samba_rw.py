# -*- coding: utf-8 -*-

import time
import os
import pytest
import shutil


def test_do():
    for i in range(10000):
        print('=============== Run test ==============%s' % i)
        srcpath='P:\\'
        readpath ='P:\\read.bin'
        copyfile = "E:/git/OS3.1/upfile/rite.bin"
        print('=============== Write ==============')
        shutil.copy(copyfile, srcpath)
        shutil.copy(readpath, "E:/git/OS3.1/upfile/")
        time.sleep(30)
        os.remove(srcpath + '/rite.bin')
        print('=============== Read ==============')
        os.remove("E:/git/OS3.1/upfile/read.bin")


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))