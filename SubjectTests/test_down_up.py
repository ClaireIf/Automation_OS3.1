# -*- coding: utf-8 -*-
import os
import time
import pytest
path ='E:\\git\\OS3.1\\test_case\\'
os.system(path+'test_downgrade.py')
time.sleep(420)
os.system(path+'test_reset.py')
time.sleep(180)
os.system(path+'test_setupD1DHCPNew.py')
time.sleep(120)
os.system(path+'test_update.py')
time.sleep(420)

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))