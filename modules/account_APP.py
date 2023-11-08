import time,logging
from appium import webdriver

class account_APP:
    def click_account(self, driver):
        time.sleep(3)
        logging.info("进入账号管理页面")
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/headIntoSelfCenter").click()
            return 1
        except Exception as e:
            logging.error('=====进入账号管理页面出错======%s' %e)
            return 0


    def unbinding(self, driver,unbindingChoose):
        time.sleep(3)
        logging.info('=======点击"解绑当前设备"==========')
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/btnUnbindCurrentDevice").click()
            if unbindingChoose == 1:
                logging.info('=====确定======')
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if unbindingChoose == 2:
                logging.info('=====取消======')
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except Exception as e:
            logging.error('=====点击解绑出错======%s' % e)
            return 0

    def addDevices(self, driver):
        time.sleep(3)
        logging.info('====点击"添加新设备"====')
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/findNewDeviceBtn").click()
            return 1
        except Exception as e:
            logging.error('======添加新设备出错========%s' % e)
            return 0

    def binding(self, driver,bindChoose):
        time.sleep(3)
        logging.info('====绑定设备====')
        try:
            if bindChoose == 1:
                logging.info('下一步')
                driver.find_element_by_id("com.diting.newifi.bridge:id/routerScanBtn").click()
                logging.info('=======等待扫描========')
                time.sleep(5)
                return 1
            if bindChoose == 2:
                logging.info('点击"关闭"图标')
                driver.find_element_by_id("com.diting.newifi.bridge:id/routerScanBack").click()
                return 2
        except Exception as e:
            logging.error('======绑定设备出错========%s' % e)
            return 0


    def binding_pw(self,driver,pw, bdpwChoose):
        time.sleep(3)
        try:
            logging.info('======绑定设备输入密码========')
            driver.find_element_by_id("com.diting.newifi.bridge:id/routerBindPwd").send_keys(pw)
            time.sleep(3)
            if bdpwChoose == 1:
                driver.find_element_by_id("com.diting.newifi.bridge:id/routerBindBtn").click()
                return 1
            if bdpwChoose == 2:
                driver.find_element_by_class_name("android.widget.ImageButton").click()
                return 2
        except Exception as e:
            logging.error('======绑定设备输入密码出错========%s' % e)
            return 0

    def binding_success(self,driver,bsChoose):
        time.sleep(2)
        try:
            driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindSuccessTxt').is_displayed()
            logging.info('===绑定成功===')
            if bsChoose == 1:
                return 1
            if bsChoose == 2:
                driver.find_element_by_class_name("android.widget.ImageButton").click()
                return 2
        except Exception as e:
            logging.error('======绑定成功出错========%s' % e)
            return 0

