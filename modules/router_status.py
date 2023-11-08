# -*- coding: utf-8 -*-

import time
import logging
import configparser
import paramiko
import json
import time
import csv
import re
import os
import sys
from tools import *
from selenium .webdriver.common.action_chains import ActionChains

class router_status:
    def check_ver(self,driver,ver,mod):
        time.sleep(1)
        try:
            logging.info('GET OS MODEL AND VERSION')
            os_ver = driver.find_element_by_id("os_version").text
            os_vers = os_ver.split('V')[1].strip()
            logging.info('OS Version= %s' % os_vers)
            print(os_vers)
            os_model = driver.find_element_by_id("os_model").text
            os_models = os_model.split('：')[1].strip()
            logging.info('OS Model = %s' % os_models)
            print(os_models)
            if os_vers == ver and os_models == mod:
                return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/check_ver-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("===Chcek Ver Error=== %s", e)
            return 0
        finally:
            pass


    ####路由状态跳转#####
    def Routing_state(self, driver, choose):
        time.sleep(2)
        try:
            if choose == 1:
                logging.info("try chick intelnetjump")
                driver.find_element_by_xpath("//*[@id=\"maincontent\"]/div/div[1]/div/a[1]").click()
                time.sleep(3)
                return 1
            if choose == 2:
                logging.info("try chick devicesjump")
                driver.find_element_by_xpath("//*[@id=\"maincontent\"]/div/div[1]/div/a[3]").click()
                time.sleep(3)
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/Routing_state-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===jump error=== %s", e)
            return 0
        finally:
            pass


    ####路由状态跳转检查#####
    def Routing_state_check(self, driver, choose):
        time.sleep(2)
        try:
            if choose == 1:
                logging.info("check intelnetjump")
                driver.find_element_by_link_text(u"互联网设置")
                return 1
            if choose == 2:
                logging.info("check devicesjump")
                driver.find_element_by_link_text(u"访问设置")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/Routing_state_check-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===jump error=== %s", e)
            return 0
        finally:
            pass


    #######安全拔出USB##########
    def PullOutUSB(self, driver):
        logging.info('Try Pull Out USB')
        time.sleep(2)
        try:
            logging.info('Click btn')
            driver.find_element_by_css_selector("#sda").click()
            try:
                time.sleep(15)
                driver.find_element_by_id('storage_no').is_displayed()
                logging.warning('Pull OUT USB Success')
                return 1
            except:
                logging.info('Pull OUT USB Fail')
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/pullout_usb-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("===Pull Out USB Error=== %s", e)
            return 0
        finally:
            pass


    def PullOutUSB_D1(self,driver):
        logging.info('Try Pull Out USB')
        time.sleep(2)
        try:
            logging.info('Click btn')
            driver.find_element_by_xpath("//*[@id=\"1\"]").click()
            time.sleep(5)
            logging.info('out usb')
            driver.find_element_by_xpath("//*[@id=\"sda\"]").click()
            logging.info('check usb')
            try:
                time.sleep(15)
                driver.find_element_by_id('storage_no').is_displayed()
                logging.warning('Pull OUT USB Success')
                return 1
            except:
                logging.info('Pull OUT USB Fail')
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/pullout_usb-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("===Pull Out USB Error=== %s", e)
            return 0
        finally:
            pass


    def client(self, driver):
        driver.find_element_by_css_selector("#sysauth > div > div > div.login-modal-content > div.modal-footer.login-modal-footer > div").click()
        time.sleep(3)
        driver.find_element_by_id("navbar-text1").click()
        time.sleep(3)
        try:
            driver.find_element_by_class_name("head-pop-des").is_displayed()
            logging.info("成功打开下载客户端界面")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/openClient-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.info('%s' % e)
            logging.info("打开下载客户端失败")
            return 0
        finally:
            pass


    def guanwangs(self, driver):
        try:
            driver.find_element_by_id("navbar-text2").click()
            now_handle = driver.current_window_handle
            all_handles = driver.window_handles
            for handle in all_handles:
                if handle != now_handle:
                    driver.switch_to_window(handle)
                    time.sleep(2)
                    driver.find_element_by_css_selector("#header > div > a > img").is_displayed()
                    logging.info("成功访问官网")
                    return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/headGuanWangs-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.info('%s' % e)
            logging.info("访问官网失败")
            return 0
        finally:
            pass