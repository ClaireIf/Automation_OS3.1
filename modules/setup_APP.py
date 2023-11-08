import time
import os,logging
from appium import webdriver

class setup_APP:
    def swipe(self,driver):
        time.sleep(2)
        try:
            driver.swipe(800, 500, 300, 500)
            return 1
        except Exception as e:
            logging.error('setup swipe error ======= %s' % e)
            return 0

    def experience(self, driver):
        time.sleep(2)
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/btn_guide_experience").click()
            return 1
        except Exception as e:
            return 0


    def binding(self, driver, bdChoose):
        try:
            logging.info(u'绑定路由器')
            time.sleep(20)
            if bdChoose ==1:
                logging.info(u'====点击“下一步”====')
                driver.find_element_by_id('com.diting.newifi.bridge:id/routerScanBtn').click()
                time.sleep(15)
                return 1
            if bdChoose ==2:
                logging.info('返回下一步')
                driver.find_element_by_id('com.diting.newifi.bridge:id/routerScanBack').click()
                return 2
            time.sleep(5)
        except:
            logging.error('绑定路由器出错')
        finally:
            pass

    def binding_other(self, driver, boChoose):
        try:
            time.sleep(15)
            if boChoose ==1:
                logging.info('绑定其他路由器')
                driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindOthers').click()
                return 1
            if boChoose ==2:
                logging.info('取消绑定其他路由器')
                driver.find_element_by_id("com.diting.newifi.bridge:id/routerConnectBack").click()
                return 2
            time.sleep(5)
        except:
            logging.error('绑定其他路由器出错')
        finally:
            pass

    def input_Router_PW(self, driver, router_pw,pwChoose):
        time.sleep(2)
        try:
            logging.info('输入路由器密码')
            driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindPwd').send_keys(router_pw)
            time.sleep(2)
            if pwChoose ==1:
                logging.info('=======绑定====')
                driver.find_element_by_id('com.diting.newifi.bridge:id/routerBindBtn').click()
                time.sleep(15)
                return 1
            if pwChoose ==2:
                logging.info('=====返回=====')
                driver.find_element_by_class_name('android.widget.ImageButton').click()
                return 2
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
