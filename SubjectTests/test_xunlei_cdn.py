import os
import time
from selenium import webdriver

down_path = r"P:\\TDDOWNLOAD\\"
tuser = '31495589#qq.com'
tpw = 'zyx7280'
down1="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5MjE5LmR5ZHl0dC5uZXQ6ODE2OS9bJUU5JTk4JUIzJUU1JTg1JTg5JUU3JTk0JUI1JUU1JUJEJUIxd3d3LnlnZHk4LmNvbV0uJUU2JTlDJTgwJUU1JTkwJThFJUU3JTlBJTg0JUU3JThFJThCLkJELjcyMHAuJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3JUU1JUI5JTk1LnJtdmJaWg=="
down2="http://dldir1.qq.com/qqfile/qq/QQ8.7/19083/QQ8.7.exe"

def login_xunlei():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://yuancheng.xunlei.com/login.html")
    time.sleep(3)
    #################################
    # jsu = "var u=\"31495589@qq.com\"; document.getElementById(\"al_u_l\").innerHTML += u;"
    # driver.execute_script(jsu)
    # time.sleep(2)
    # jsp = "var p=\"zyx7280\"; document.getElementById(\"al_p_l\").innerHTML += p;"
    # driver.execute_script(jsp)
    # time.sleep(2)
    # driver.find_element_by_id("al_submit").click()
    ###############################
    # driver.find_element_by_id("al_u").clear()
    # driver.find_element_by_id("al_u").send_keys(tuser)
    # time.sleep(3)
    # driver.find_element_by_id("al_p").clear()
    # driver.find_element_by_id("al_p").send_keys(tpw)
    # time.sleep(3)
    # driver.find_element_by_id("al_submit").click()
    driver.switch_to_alert("xls_quick_login")
def add_file():
    time.sleep(20)
    driver.find_element_by_css_selector("#tasklist-toolbox > ul > li:nth-child(1) > a.site_new > span").click()
    time.sleep(10)
    driver.find_element_by_id("pop-newtask-multi-url").send_keys(down2)
    time.sleep(5)
    driver.find_element_by_id("pop-newtask-submit").click()

while True:
    login_xunlei()
    add_file()
    files = os.listdir(down_path)
    print(files)
    for i in range(10000):
        print(i)
        for file in files:
            print(file)
            if file == 'test.txt':
                os.remove('P:\\TDDOWNLOAD\\test.txt')
                break
            else:
                continue
        time.sleep(60)

