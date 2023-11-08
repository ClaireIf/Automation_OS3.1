import paramiko,sys,time,configparser,os,re,logging
sys.path.append("..")
from tools import *
from selenium import webdriver
import conftest

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
cmd = "ps|grep pear"
check_progress = ['pear_restart','pear_update','pear_monitor','pear_webrtc','pear_fuse']

driver = webdriver.Chrome()
time.sleep(1)
driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
driver.quit()

def test_pear_monitor():
    # conftest.browser()
    # driver = conftest.driver
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22, "root", default_pw)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    ps_pear = stdout.readlines()
    ssh.close()
    ps_pear =str(ps_pear)
    print(ps_pear)
    logging.info(ps_pear)
    count = len(check_progress)
    fail = 0
    for i in range(count):
        logging.info('=======check progress ===========')
        check_pear = re.compile(check_progress[i])
        result = check_pear.search(ps_pear)
        if result:
            # print(result.string)
            print('==========Find==========%s' % check_progress[i])
            logging.info('===========Find===========%s' % check_progress[i])
        else:
            fail = fail +1
            print('====== ON========%s' %fail)
            logging.info('%s====== ON Find========%s' % (check_progress[i], fail))


while True:
    test_pear_monitor()
    time.sleep(30)