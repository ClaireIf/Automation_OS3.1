import paramiko,time,os,configparser,sys
from selenium import webdriver
sys.path.append("..")
from tools import *
t = tools()

projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
degrade = "sed -i \"s/option ver '.*'/option ver \'3.2.1.0000\'/g\" /etc/config/system"
restart_rcpd="/etc/init.d/rcpd restart"

t.ssh_cmdss(default_ip,default_pw,degrade)
time.sleep(3)
t.ssh_cmdss(default_ip,default_pw,restart_rcpd)