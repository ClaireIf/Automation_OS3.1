import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://yuancheng.xunlei.com")
time.sleep(10)
js = "document.getElementById('al_warn').style.display='block';"
driver.execute_script(js)

driver.find_element_by_id("al_u_l").send_keys("test")