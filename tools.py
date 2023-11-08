import os
import csv
import sys
import time
import urllib.request
import paramiko
import logging
import re
import configparser


class tools:
    #####ping#####
    def ping(self,address):
        time.sleep(2)
        ping = os.system("ping %s" %address)
        logging.info("ping return %s" % ping)
        if ping == 0:
            ###ping 返回0 为成功####
            logging.info("ping %s success" %address)
            return 0
        elif ping == 1:
            ###ping 返回1 为失败####
            logging.error("ping %s fail" % address)
            return 1

    def urlRequest(self, url):
        try:
            testUrl=urllib.request.Request('http://'+"%s" %url)
            openUrl=urllib.request.urlopen(testUrl)
            codeNum=openUrl.getcode()
            logging.info('Code Num == %s' % codeNum)
            if codeNum == 200:
                return 1
        except:
            return 0


    def open_http(self, httpurl):
        time.sleep(2)
        try:
            req = urllib.request.Request("http://" +httpurl)
            f = urllib.request.urlopen(req)
            s = f.read()
            getcodes = s.decode('gbk','ignore')
            getcodes = f.getcode()
            logging.info(getcodes)

            if getcodes == 200:
                logging.info("open http success")
                return 1
            else:
                logging.info("open http fail")
                return 2
        except Exception as e:
            logging.info(e)


    ###访问Samba###
    def open_smaba(self):
        time.sleep(2)
        samba = os.path.exists("S:\\")
        if samba == True:
            logging.info("open Smaba success")
            return 1
        else:
            logging.error("open Smaba fail")
            return 0

    def get_config(self, lines):
        d = {}
        for i in list(map(lambda x: x.strip().split('='), lines)):
            if len(i) == 2:
                d.update({i[0]: i[1]})
        return d


    def write_ser_log(self, log, file):
        if log is not None:
            log = log.replace("\\r", "")
            log = log.replace("\\n", "")
            log = log.replace("b'", "")
            log = log.replace("'", "")
            log = log.strip()
            file.write(log + "\n")
            file.flush()
            print(log)
        else:
            pass

    def get_test_ip(self):
        get_ipALL = os.popen("nbtstat -a IP").readlines()
        print(get_ipALL)
        for get_ipALL1 in get_ipALL:
            get_ip = re.match(("(.*)\[(.*)\](.*)\[(.*)\](.*)"), get_ipALL1)
            if get_ip:
                get_ip1 = get_ip.group(2)
                # print(get_ip.group(2))
                get_ip2 = re.findall('[0-9]+', get_ip.group(2))
                # print(get_ip2[0])
                if get_ip2[0] == '192':
                    logging.info(get_ip1)
                    dmz_ip = get_ip1.split(".")[-1]
                    dmzip1 = get_ip1.split(dmz_ip)[0]
                    logging.info(dmz_ip)
                    logging.info(dmzip1)
                    get_path = os.path.dirname(os.getcwd())
                    config_path = get_path + '\\configure'
                    configfile = config_path + '\\' +  'testconfig.ini'
                    logging.info(configfile)
                    config = configparser.ConfigParser()
                    config.read(configfile, encoding='UTF-8')
                    # config.set('SystemInfo', 'lan_ip', get_ip1)
                    config.set('DMZ', 'dmz_ip',dmz_ip)
                    config.set('DMZ', 'dmzip1',dmzip1)
                    config.write(open(configfile, 'w', encoding='UTF-8'))


    def uci_cmd(self,ssh_connection, cmd, flag):
        stdin, stdout, stderr = ssh_connection.exec_command(cmd)
        for l in stdout.readlines():
            if l.split('=')[0] == flag:
                return l.split("=")[1]
            else:
                pass
        return None


    def find_flag(self,lines, flag):
        return [l for l in lines if l.find(flag) > -1]


    ####调用SSH终端命令###
    def ssh_cmd(self, ip, pw, cmd, cmdChoose):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, "root", pw)
        if cmdChoose == 1:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            ssh.exec_command(stdout.readlines())
        if cmdChoose == 2:
            ssh.exec_command(cmd)
        ssh.close()
        #time.sleep(150)

    def ssh_cmdss(self,ip,password, cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, "root", password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return stdout.readlines()


    ###日志输出###
    def log(self, filename):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=os.path.dirname(os.getcwd())+"/logfile/"+filename+'.log',
                            filemode='a')
        #################################################################################################
        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        # if not logging.getLogger('').handlers:
        logging.getLogger('').addHandler(console)
        # logging.getLogger('').removeHandler(console)
        logging.getLogger('').handlers.pop()####不显示在html上，不重复打印
        #################################################################################################


    ###错误截图###
    def errorpng(self, driver, filename):
        ####
        #获取project_path=sys.path[0]
        ####
        ####
        #获取文件名称filename=os.path.basename(__file__).split('.')[0]
        ####
        driver.get_screenshot_as_file(sys.path[2] + "/OS3.1/errorpng/" + filename + "%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))


    def autoresult(self,filename, ar):
        excl = open("AutoResult.csv", 'a+', newline='')
        first = [filename, ar]
        csvwriter = csv.writer(excl, dialect='excel')
        csvwriter.writerow(first)
