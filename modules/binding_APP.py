import time
import os,logging
from appium import webdriver

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

def input_Router_PW(driver,router_pw):
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
        driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/test_binding-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
        logging.error('绑定失败')
        return 2
    finally:
        pass
