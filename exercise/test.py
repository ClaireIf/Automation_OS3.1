# -*- coding:utf-8 -*-
import time
import logging
import urllib.request
import os
import sys
import csv
import paramiko
import re
# sys.path.append("..")
# from tools import *
# # import re
# import test_setupDHCP
# from selenium import webdriver
#filename = os.path.basename(__file__).split('.')[0]
# filename =sys.path[0]+"/logfile/"
# print(filename)
# tools().logging(filename,switch=1)
# import os
# # import glob
# # dirs = os.path.abspath(".")
# # print(dirs)
#
# # lists = glob.glob(dirs+"\\*.*")
# # for t in lists:
# #     # print(os.path.basename(t))
# #     print (t)
# #     dotIndex = t.index(".")
# #     print (dotIndex)
# #     print (t[:dotIndex])
# #     input()
# x=os.path.basename(__file__).split( )[0]
# print(x)

############
##测试截图##
############
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.get_screenshot_as_file(sys.path[0]+"/errorpng/"+filename+"%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
# driver.close()

############
##写excel##
############
# excl = open("AutoResult.csv", 'a+', newline='')
# first = [__file__, 'Auto13 Success']
# csvwriter = csv.writer(excl, dialect='excel')
# csvwriter.writerow(first)

############
##获取目录##
############
# print(sys.path)
# print(os.getcwd())
# print(sys.argv[0])
# print(__file__)
# print(__file__.split('.py')[0])
# print(sys.path[2])
# print(os.path.basename(__file__).split('.')[0])
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
# print(os.path.dirname(os.getcwd()))
# print(os.path.basename(__file__))
# print(sys.path)


############
##SSH判断wifi是否开启##
############
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.99.1', 22, "root", '12345678')
# ssid_cmd = ["iwconfig ra0", "iwconfig rai0"]
# for ssid_cmd in ssid_cmd:
#     stdin, stdout, stderr = ssh.exec_command(ssid_cmd)
#     print(stdout.readlines())
#     lists = str.strip(stdout.readlines()[1])
#     print(lists)
#     ssh.close()
#     if lists == 'Link Quality:0  Signal level:0  Noise level:0':
#         print('close')
#     else:
#         print('open')


# for i in range(3):
#
#     if i == '2':
#         pass
#     else:
#         x = 1
#         x = x + 1
#         print(i)


# x = ['a','b']
# for i in  x:
#     print(i)
#     print(x)
# import logging
# import json
# # print(os.path.dirname(os.getcwd()))
# t = tools()
# projectpath = os.path.dirname(os.getcwd())
# config_file = projectpath + '/configure/' + 'testconfig.ini'
# filename = os.path.basename(__file__).split('.')[0]
# t.log(filename)
# newifilog=os.popen('net view').read()
# if 'newifi' in newifilog:
#     print('x')
# logging.info(newifilog)

# import os
# import re
# get_ipALL = os.popen("nbtstat -a IP").readlines()
# print(get_ipALL)
# for get_ipALL1 in get_ipALL:
#     get_ip = re.match(("(.*)\[(.*)\](.*)\[(.*)\](.*)"),get_ipALL1)
#     if get_ip:
#         get_ip1 = get_ip.group(2)
#         # print(get_ip.group(2))
#         get_ip2 = re.findall('[0-9]+', get_ip.group(2))
#         # print(get_ip2[0])
#         if get_ip2[0] == '192':
#             print(get_ip1)
#     print('+++++++++++++++++++++++++++++++++')



from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file("test.png")


