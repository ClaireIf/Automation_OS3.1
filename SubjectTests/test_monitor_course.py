import time,os,logging,configparser,paramiko
import sys
sys.path.append("..")
from tools import *

t = tools()
projectPath = os.path.dirname(os.getcwd())
configFile = projectPath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)
config = configparser.ConfigParser()
config.read(configFile, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
cmds = ["ps | grep xCloudClient", "ps | grep xcloud_manager", "ps |grep smbd", "ps |grep minidlna", "ps |grep miniupnpd"]

def ssh_getResult():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22 , "root", default_pw)
    fail = 0
    while True:
        for cmd in cmds:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # logging.info(stdout.readlines())
            list = stdout.readlines()
            for result in list:
                logging.info("==============================")
                logging.info(result)
                get_course_type = str.split(result)[3]
                get_course = str.split(result)[4]
                if get_course_type == 'S':
                    if get_course == "/usr/local/xcloud/bin/xCloudClient":
                        logging.info("xCloudClient ====== OK")
                    if get_course == "/usr/sbin/xcloud_manager":
                        logging.info("xcloud_manager ======= OK")
                    if get_course == "/usr/sbin/smbd":
                        logging.info("smbd ======= OK")
                    if get_course == "/usr/bin/minidlna":
                        logging.info("minidlna ======== OK")
                    if get_course == "/usr/sbin/miniupnpd":
                        logging.info("miniupnpd ======= OK")
                elif get_course_type == 'R':
                    pass
                else:
                    fail = fail + 1
                    logging.info("fail ============ %s" % fail)
        time.sleep(10)

ssh_getResult()
