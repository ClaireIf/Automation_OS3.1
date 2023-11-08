import time
from selenium import webdriver

def unbind():
    driver = webdriver.Chrome()
    try:
        driver.get('http://192.168.99.1:14000/api?method=set_xc_logout')
        time.sleep(10)
        driver.close()
        driver.quit()
    except:
        pass

unbind()