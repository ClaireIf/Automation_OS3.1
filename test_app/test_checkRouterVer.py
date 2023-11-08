import paramiko,time,os,configparser,sys,logging
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
version = config.get('Upgrade', 'new_version')
cat_ver = "cat /etc/openwrt_version"

Ver=t.ssh_cmdss(default_ip,default_pw,cat_ver)
print(str.strip(Ver[0]))
if str.strip(Ver[0]) != version:
    logging.info('============upgrade success==========')
else:
    logging.info("============upgrade fail==========")