import time
import os,logging
from appium import webdriver
import sys
sys.path.append("..")
from tools import *

router_pw = '12345678'

t = tools()
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
#####################################################

def startApp():
    ######### start App #######
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.0'
    desired_caps['deviceName'] = 'U4FEROE6YPUKQGTO'
    desired_caps['appPackage'] = 'com.diting.newifi.bridge'
    desired_caps['appActivity'] = 'com.diting.xcloud.app.widget.activity.WelcomeActivity'
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyBoard"] = True
    desired_caps["noReset"] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)
    return driver

def bingding(driver):
    try:
        print(u'绑定路由器')
        logging.info(u'绑定路由器')
        time.sleep(15)
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerScanBtn').click()
        time.sleep(15)
    except:
        pass

def bingding_other(driver):
    try:
        time.sleep(15)
        print(u'绑定其他路由器')
        logging.info('绑定其他路由器')
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindOthers').click()
        time.sleep(5)
    except:
        pass

def input_Router_PW(driver):
    time.sleep(2)
    try:
        print(u'输入路由器密码')
        logging.info('输入路由器密码')
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindPwd').send_keys(router_pw)
        time.sleep(2)
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindBtn').click()
        time.sleep(15)
    except:
        pass

def check_binding(driver):
    time.sleep(15)
    try:
        print(u'检查是否绑定')
        logging.info('检查是否绑定')
        driver.find_element_by_id('com.diting.newifi.bridge:id/layout_miningActionView').is_displayed()
        print(u'绑定成功')
        logging.info('绑定成功')
        return 1
    except:
        driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/test_binding-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
        print(u'绑定失败')
        logging.error('绑定失败')
        return 2



def closed(driver):
    driver.close_app()
    driver.quit()

fail = 0
for i in range(1000):
    driver = startApp()
    print('test count ==%s' %i)
    logging.info('test count ==%s' %i)
    bingding_other(driver)
    bingding(driver)
    input_Router_PW(driver)
    if check_binding(driver) == 1:
        os.system('test_reset.py')
        time.sleep(180)
        os.system('test_setupD1DHCPNew.py')
    else:
        fail = fail + 1
    closed(driver)
    print('fail count===%s' %fail)
    logging.info('fail count===%s' %fail)
    print(fail)
    if fail == 20:
        break

