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
switch_cmd = "uci show wireless.ra0"
switch_cmd_5G = "uci show wireless.rai0"

def getWiFi_5G_Switch():
    switch=t.ssh_cmdss(default_ip, default_pw, switch_cmd_5G)
    # print(switch[-1])
    print(str.strip(switch[-1]))
    if str.strip(switch[-1]) == "wireless.rai0.disabled='1'":
        logging.info('============rai0 close==========')
        return 1
    else:
        logging.info("============rai0 open==========")
        return 0


def getWiFi_24G_Switch():
    switch=t.ssh_cmdss(default_ip, default_pw, switch_cmd_5G)
    # print(switch[-1])
    print(str.strip(switch[-1]))
    if str.strip(switch[-1]) == "wireless.rai0.disabled='1'":
        logging.info('============rai0 close==========')
        return 1
    else:
        logging.info("============rai0 open==========")
        return 0