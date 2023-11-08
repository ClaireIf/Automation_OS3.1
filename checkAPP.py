import os
import re
import datetime
import time
import shutil
import configparser


def checkAPP():
    result_dir = "A:\\"
    l = os.listdir(result_dir)
    bulid = l[-1]
    print(bulid)
    version = bulid.split("_v")[1]
    # print(version)
    new_version = version.split(".apk")[0]
    print(new_version)
    localFile = result_dir + bulid
    mobileFile = "sdcard/"
    os.system("adb uninstall com.diting.newifi.bridge")
    # os.system("adb push %s %s" % (localFile,mobileFile))
    os.system("adb install -r -d %s" % result_dir+bulid)
    print(localFile + '===copy ==> ' + mobileFile)
    projectpath = os.getcwd()
    # print(projectpath)
    Project_Path = projectpath
    # print('Project_path=%s' % Project_Path)
    uppath = 'sdcard/' + bulid
    # print(uppath)
    config_file = Project_Path + '\\configure\\' + 'testconfig_app.ini'
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    config.set('APP', 'app_path', uppath)
    config.set('APP', 'version', new_version)
    config.write(open(config_file, 'w', encoding='UTF-8'))

checkAPP()