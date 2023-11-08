import time,logging
from appium import webdriver

class download_APP:
    def click_download(self,driver):
        time.sleep(2)
        try:
            logging.info('=====点击进入"下载"页面======')
            driver.find_element_by_id("com.diting.newifi.bridge:id/radBtn_Download")
            return 1
        except Exception as e:
            logging.error('=====点击下载出错=====%s' % e)
            return 0

    def get_down(self, driver):
        time.sleep(2)
        try:
            return 1
        except Exception as e:
            logging.error('=====点击下载出错=====%s' % e)
            return 0


    def click_addDown(self, driver):
        time.sleep(2)
        try:
            logging.info('=======点击"+"========')
            driver.find_element_by_id("com.diting.newifi.bridge:id/mVideoImageMore").click()
            return 1
        except Exception as e:
            logging.error('=====添加任务出错=====%s' % e)
            return 0

    def addDown_link(self, driver, link, linkChoose):
        time.sleep(2)
        logging.info('=== 点击"添加下载链接任务" ===')
        driver.find_element_by_id("com.diting.newifi.bridge:id/newurltask").click()
        try:
            logging.info('====填写link任务链接====')
            driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtBTContent").send_keys(link)
            if linkChoose == 1:
                logging.info('===点击下载===')
                driver.find_element_by_id("com.diting.newifi.bridge:id/btnDownload").click()
            if linkChoose == 2:
                logging.info('====点击后退====')
                driver.find_element_by_id("android.widget.ImageButton").click()
        except Exception as e:
            logging.error('=====添加下载链接任务出错=====%s' % e)
            return 0

    def addDown_bt(self, driver, btChoose):
        time.sleep(2)
        driver.find_element_by_id("com.diting.newifi.bridge:id/newbtask").click()
        try:
            if btChoose == 1:
                driver.find_element_by_id().click()
                return 1
            if btChoose == 2:
                logging.info('====点击后退====')
                driver.find_element_by_class_name("android.widget.ImageButton").click()
                return 2
        except Exception as e:
            logging.error('=====添加下载BT任务出错=====%s' % e)
            return 0


