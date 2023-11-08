import time,logging
from appium import webdriver

def enter_register(driver):
    try:
        driver.find_element_by_id('com.diting.newifi.bridge:id/btnLogin').is_displayed()
        return 1
    except:
        return 2


def register(driver,user,pw):
    try:
        driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtAccount").clear()
        driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtAccount").send_keys(user)
        time.sleep(2)
        driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtPwd").clear()
        driver.find_element_by_id("com.diting.newifi.bridge:id/edtTxtPwd").send_keys(pw)
        time.sleep(2)
        driver.find_element_by_id("com.diting.newifi.bridge:id/btnNext").click()
        return 1
    except:
        logging.error("=======注册失败=======")
        return 2