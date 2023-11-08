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
open_cdn_cmd = "ubus call xapi.basic set_cdn_switch '{\"switch\":\"1\"}'"
get_cdn_cmd = "ubus call xapi.basic get_cdn_status '{}'"

print(t.ssh_cmdss(default_ip,default_pw,open_cdn_cmd))
print(t.ssh_cmdss(default_ip,default_pw,get_cdn_cmd))