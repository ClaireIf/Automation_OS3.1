# -*- coding:utf-8 -*-
###################################
#   登录路由管理页面
###################################
import logging
import time
import pytest
import os
from selenium.webdriver.support.ui import Select

class login_router:
    ###打开网址###
    def open_url(self, driver, url):
        ###返回1为欢迎界面，返回2为初始化界面####
        try:
            logging.info("try open " + url)
            driver.get(url)
            time.sleep(5)
            try:
                driver.find_element_by_class_name("login-logo").is_displayed()
                logging.info("enter welcome")
                return 1
            except:
                driver.find_element_by_id("check-btn").is_displayed()
                logging.info("enter initialize")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/open_url%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===open url error=== %s", e)
            return 0
        finally:
            pass


    ####管理员密码登录###
    def login(self, driver, default_pw):
        time.sleep(2)
        try:
            logging.info("=== Login password === %s " % default_pw)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(default_pw)
            time.sleep(1)
            logging.info('click login btn')
            driver.find_element_by_css_selector("#sysauth > div > div > div.login-modal-content > div.modal-footer.login-modal-footer > div").click()
            time.sleep(5)
            try:
                ###检查是否登录成功,检测路由状态元素###
                logging.info('check login ')
                driver.find_element_by_css_selector("#mainmenu > ul > li.item-active > a > span").is_displayed()
                logging.info("login success")
                return 1
            except:
                logging.info("login fail")
                return 0
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/login%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===login error=== %s", e)
            return 0
        finally:
            pass


    def footer(self,driver):
        time.sleep(2)
        try:
            logging.info("test router footer")
            
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/footer-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===test router footer error=== %s", e)
            return 0
        finally:
            pass


    #####页脚-官网#####
    def guanwang(self,driver):
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[2]/a")
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[2]/a").click()
        time.sleep(5)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                time.sleep(2)
        guanwang_Actual_address = driver.current_url
        logging.info('=== Get Address === %s'% guanwang_Actual_address)
        guanwang_Standard_address = "http://www.newifi.com/"
        logging.info('=== GuanWang Address === %s'% guanwang_Standard_address)
        if guanwang_Actual_address == guanwang_Standard_address:
            logging.info("guanwang_ok")
            return 1
        else:
            logging.info("guanwang_faill")
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/guanwang-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0


    #####页脚-微博#####
    def weibo(self,driver):
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[3]/a").click()
        time.sleep(10)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                time.sleep(2)
        weibo_Actual_address = driver.current_url[:25]
        logging.info(weibo_Actual_address)
        weibo_Standard_address = "http://weibo.com/xyxcloud"
        logging.info(weibo_Standard_address)
        if weibo_Actual_address == weibo_Standard_address:
            logging.info("weibao_ok")
            return 1
        else:
            logging.info("weibao_faill")
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/weibo-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0

    def weibos(self, driver):
        weibo_url = driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[3]/a").get_attribute("href")
        logging.info('get weibo url = %s' % weibo_url)
        if weibo_url == 'http://weibo.com/xyxcloud?topnav=1&wvr=58&topsug=1':
            logging.info('weibo ====ok')
            return 1
        else:
            logging.error('weibo ===fail')
            return 0

    #####页脚-社区#####
    def shequ(self,driver):
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[5]/a")
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[5]/a").click()
        time.sleep(5)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                time.sleep(2)
        shequ_Actual_address = driver.current_url
        logging.info(shequ_Actual_address)
        shequ_Standard_address = "http://bbs.newifi.com/"
        logging.info(shequ_Standard_address)
        if shequ_Actual_address == shequ_Standard_address:
            logging.info("shequ_ok")
            return 1
        else:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/shequ-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("shequ_faill")
            return 0


