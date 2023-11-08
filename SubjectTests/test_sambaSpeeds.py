# -*- coding: utf-8 -*-

import os
import shutil
import threading
import time  # 引入time模块

# copystart = time.time()
# print("当前时间戳为:", copystart)
# time.sleep(1)
# copyend = time.time()
# print("当前时间戳为:", copyend)
# copytime = copyend - copystart
# print(copytime)


samba = r"S:\\"
# create 512M file
size = 1024 * 1024 * 512
with open("test.txt", 'wb') as f:
    f.write(os.urandom(size))
copystart = time.time()
print("当前时间戳为:", copystart)
shutil.copy('test.txt', samba)
copyend = time.time()
print("当前时间戳为:", copyend)
copytime = copyend - copystart
print(copytime)
SambaW = size / copytime
print(SambaW)
