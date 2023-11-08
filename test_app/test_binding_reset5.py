import time
import os,logging
import sys
sys.path.append("..")
from tools import *
from appium import webdriver

router_pw = '12345678'

t = tools()
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
#####################################################

def startApp():
    try:
        logging.info('启动APP')
        ######### start App #######
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.0'
        desired_caps['deviceName'] = 'W8RDU15625028444'
        desired_caps['appPackage'] = 'com.diting.newifi.bridge'
        desired_caps['appActivity'] = 'com.diting.xcloud.app.widget.activity.WelcomeActivity'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyBoard"] = True
        desired_caps["noReset"] = True
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver
    except:
        logging.error('启动APP失败')
    finally:
        pass

def bingding(driver):
    try:
        logging.info(u'绑定路由器')
        time.sleep(15)
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerScanBtn').click()
        time.sleep(15)
    except:
        logging.error('绑定路由器出错')
    finally:
        pass

def bingding_other(driver):
    try:
        time.sleep(15)
        logging.info('绑定其他路由器')
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindOthers').click()
        time.sleep(5)
    except:
        logging.error('绑定其他路由器出错')
    finally:
        pass

def input_Router_PW(driver):
    time.sleep(2)
    try:
        logging.info('输入路由器密码')
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindPwd').send_keys(router_pw)
        time.sleep(2)
        driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindBtn').click()
        time.sleep(15)
    except:
        logging.error('输入路由器密码出错')
    finally:
        pass

def check_binding(driver):
    time.sleep(15)
    try:
        logging.info('检查是否绑定')
        driver.find_element_by_id('com.diting.newifi.bridge:id/layout_miningActionView').is_displayed()
        logging.info('绑定成功')
        return 1
    except:
        driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/test_bindingssss-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
        logging.error('绑定失败')
        return 2
    finally:
        pass

def closed(driver):
    try:
        logging.info('关闭APP')
        driver.close_app()
        driver.quit()
    except:
        logging.error('关闭APP出错')
    finally:
        pass


fail = 0
success = 4
for i in range(1000):
    driver = startApp()
    print('test count ==%s' %i)
    logging.info('test count ==%s' %i)
    bingding_other(driver)
    bingding(driver)
    input_Router_PW(driver)
    if check_binding(driver) == 1:
        success = success +1
        print('success ===%s' %success)
        logging.info('success ===%s' %success)
        if success ==5:
            print('如果成功5次，则重置路由器')
            logging.info('如果成功5次，则重置路由')
            os.system("py.test E:\\git\OS3.1\\test_case\\test_reset.py")
            time.sleep(180)
            os.system('py.test E:\\git\OS3.1\\test_case\\test_setupD1DHCPNew.py')
            time.sleep(60)
            success = 0
        else:
            os.system('test_unbind.py')
            time.sleep(10)
    else:
        fail = fail + 1
    closed(driver)
    print('fail count===%s' %fail)
    logging.info('fail count===%s' %fail)
    print(fail)
    if fail == 20:
        break


