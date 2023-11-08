import time,logging
from appium import webdriver

class login_APP:
    def check_login(self,driver):
        logging.info('检查是否进入APP注册、登录选择页面')
        try:
            driver.find_element_by_id('com.diting.newifi.bridge:id/btnLogin').is_displayed()
            logging.info('进入APP注册、登录选择页面')
            return 1
        except Exception as e:
            logging.info('未进入进入APP注册、登录选择页面====%s' %e)
            return 2

    def enter_login(self,driver):
        logging.info(u'======点击已有账号，直接登录=====')
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/btnLogin").click()
            return 1
        except:
            return 2


    def login(self, driver, user, pw):
        try:
            logging.info('输入登录账号')
            driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtAccount").clear()
            driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtAccount").send_keys(user)
            time.sleep(3)
            logging.info('输入登录密码')
            driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtPwd").clear()
            driver.find_element_by_id('com.diting.newifi.bridge:id/edtTxtPwd').send_keys(pw)
            time.sleep(3)
            logging.info('点击登录按钮')
            driver.find_element_by_id('com.diting.newifi.bridge:id/btnLogin').click()
        except Exception as e:
            logging.info('登录出错======%s' % e)

    def click_register(self,driver):
        logging.info('====点击登录页面内的“注册”按钮====')
        driver.find_element_by_id("com.diting.newifi.bridge:id/btnRegLink").click()
        try:
            logging.info("======检查是否进入注册页面======")
            driver.find_element_by_id("com.diting.newifi.bridge:id/btnNext").is_displayed()
            logging.info("=====进入注册页面=====")
            return 1
        except:
            logging.error("=====未进入注册页面======")
            return 2


    def startApp(self,platformVersion,deviceName):
        try:
            ######### start App #######
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = platformVersion
            desired_caps['deviceName'] = deviceName
            desired_caps['appPackage'] = 'com.diting.newifi.bridge'
            desired_caps['appActivity'] = 'com.diting.xcloud.app.widget.activity.WelcomeActivity'
            desired_caps["unicodeKeyboard"] = True
            desired_caps["resetKeyBoard"] = True
            desired_caps["noReset"] = True
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(10)
            return driver
        except:
            logging.error('启动APP出错')


    def closed(self,driver):
        try:
            logging.info('关闭APP')
            driver.close_app()
            driver.quit()
        except:
            logging.info('关闭出错')

