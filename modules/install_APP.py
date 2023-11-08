import time,logging,os
import base64
from appium import webdriver

class install_APP:
    def install_app(self, driver, app_path):
        time.sleep(2)
        try:
            driver.install_app(app_path)
            return 1
        except Exception as e:
            return 0

    def uninstall_app(self, driver):
        time.sleep(2)
        try:
            driver.remove_app("com.diting.newifi.bridge")
            return 1
        except Exception as e:
            return 0

    def push_app(self, localFile, mobileFile):
        time.sleep(2)
        try:
            os.system("adb push %s %s" %localFile %mobileFile)
            return 1
        except Exception as e:
            return 0

