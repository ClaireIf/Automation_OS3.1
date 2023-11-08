import time,logging
from appium import webdriver

class homepage_APP:
    def clickCDN(self,driver):
        time.sleep(13)
        logging.info('====点击进入CDN页面====')
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/layout_frame_mining").click()
            return 1
        except Exception as e:
            logging.info('=====点击进入CDN出错====%s' %e)
            return 0


    def checkCDN(self, driver):
        time.sleep(2)
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/startJewelFieldBtn").is_displayed()
            logging.info('=====弹出立即开启CDN页面=====')
            return 1
        except Exception as e:
            logging.error('=====没有弹出立即开启CDN页面====%s' %e)
            return 0

    def click_openCDN_set(self, driver):
        time.sleep(3)
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/jewelFieldSetBtn").click()
            time.sleep(2)
            return 1
        except Exception as e:
            return 0

    def openCDN_set(self, driver):
        time.sleep(3)
        try:
            logging.info("==========开启CDN挖矿============")
            driver.find_element_by_id("com.diting.newifi.bridge:id/openJewelFieldBtn").click()
            return 1
        except:
            logging.error('=====开启CDN挖矿出错==========')
            return 0

    def get_openCDN(self, driver):
        time.sleep(3)
        try:
            x=driver.find_element_by_id("com.diting.newifi.bridge:id/openJewelFieldBtn").get_attribute("id")
            print(x)
        except Exception as e:
            return 0

    def openCDN(self,driver):
        time.sleep(2)
        logging.info('========点击“立即开启”=========')
        try:
            driver.find_element_by_id('com.diting.newifi.bridge:id/startJewelFieldBtn').click()
            return 1
        except Exception as e:
            logging.error('======点击开启出错====%s' %e)
            return 0

    def cancelCDN(self, driver):
        time.sleep(2)
        logging.info("=====取消开启CDN======")
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/jewelFieldActivityExplainCancelBtn").click()
            return 1
        except Exception as e:
            logging.error('======取消CDN出错=====%s' %e)
            return 0