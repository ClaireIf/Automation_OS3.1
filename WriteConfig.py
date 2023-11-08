#  -*- coding: utf-8 -*-
import configparser
import os
import re
model = 'y2'
test_mac = '20:76:93:3e:88:81'
test_mac1= re.findall('[a-zA-Z0-9]+',test_mac)
default_ssid = 'newifi_' + test_mac1[-2] + test_mac1[-1]
print(default_ssid)
get_path = os.getcwd()
print(get_path)
errorpng_path = get_path + '\\errorpng'
caseFailpng_path = errorpng_path + '\\caseFail'
upfile_path = get_path + '\\upfile'
logfile_path = get_path + '\\logfile'

config_path = get_path + '\\configure'
configfile = config_path + '\\'+ model + '_testconfig.ini'
config = configparser.ConfigParser()
config.read(configfile, encoding='UTF-8')
config.set('Default', 'default_ssid', default_ssid)
config.set('Default', 'default_guest', default_ssid + '_guest')
config.set('Path', 'projectpath', get_path)
config.set('Path', 'errorpath', errorpng_path)
config.set('Path','casefail', caseFailpng_path)
config.write(open(configfile, 'w',encoding='UTF-8'))
