import paramiko,time,os,configparser,sys,logging
from selenium import webdriver
sys.path.append("..")
from tools import *
t = tools()

projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = 10
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
top_cmd = "top -n 15000>>/mnt/sda1/top.log"
t.ssh_cmdss(default_ip,default_pw,top_cmd)

