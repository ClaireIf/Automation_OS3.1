import os
import re
import datetime
import time
import shutil
import configparser


def checkFiremware():
    result_dir = "U:\\"
    l = os.listdir(result_dir)
    st = l.sort(key=lambda fn: os.path.getmtime(result_dir  + fn) if not os.path.isdir(result_dir  + fn) else 0)  # 第二句
    d = datetime.datetime.fromtimestamp(os.path.getmtime(result_dir  + l[-1]))
    # print(('last file is ' + l[-1]))
    bulid = l[-1]
    print(bulid)
    version = bulid.split("_")[3]
    new_version = version.split("v")[1]
    upfile = result_dir + bulid
    shutil.copy(upfile, 'upfile')
    print(upfile + '===copy ==> upfile')
    projectpath = os.getcwd()
    print(projectpath)
    Project_Path = projectpath
    print('Project_path=%s' % Project_Path)
    uppath = Project_Path + '\\upfile\\' + bulid
    print(uppath)
    config_file = Project_Path + '\\configure\\' + 'testconfig.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    config.set('Upgrade', 'new_build', uppath)
    config.set('Upgrade', 'new_version', new_version)
    config.write(open(config_file, 'w', encoding='UTF-8'))

checkFiremware()