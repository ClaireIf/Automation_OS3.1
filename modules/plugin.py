# -*- coding:utf-8 -*-
import time
import logging
import paramiko
import json
import time
import re
import os
import sys
from selenium .webdriver.common.action_chains import ActionChains


class plugin():
    ###本地安装插件####
    def localPlugin(self,driver,plugin_path,pluginChoose):
        #time.sleep(15)
        ##########
        logging.info('===========enter local plugin===============')
        driver.find_element_by_xpath("//*[@id=\"viewmenu\"]/ul/li[3]/a").click()
        time.sleep(5)
        try:
            logging.info("up xipk")
            driver.find_element_by_id("plugin_local_file").send_keys(plugin_path)
            time.sleep(10)
            if pluginChoose == 1:
                getInstallInfo = driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > p").text
                if getInstallInfo =='经检测，您已安装过该应用，是否覆盖安装？':
                    return 3
                logging.info('sure xipk')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
                time.sleep(20)
                logging.info('click installed plugin')
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(2) > a").click()
                time.sleep(5)
                logging.info('Get plugin Info')
                plugintitle = driver.find_element_by_css_selector("#map > div:nth-child(2) > div.plugins-f > div > p.plugins-title").text
                logging.info(plugintitle)
                if plugintitle == u'迅雷远程下载通用版':
                    return 1
            if pluginChoose == 2:
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel").click()
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/localPlugin-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Local Plugin Error === %s", e)
            return 0
        finally:
            pass


    ###在线安装插件####
    def onlinePlugin(self,driver):
        time.sleep(2)
        try:
            logging.info('=========enter plugin===========')
            driver.find_element_by_xpath("//*[@id=\"mainmenu\"]/ul/li[3]/a/div").click()
            time.sleep(30)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/Plugin_online-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Online Plugin Error === %s", e)
            return 0
        finally:
            pass


    ######已安装##########
    def installedPlugin(self,driver):
        time.sleep(2)
        try:
            logging.info('========installed plugin======')
            # driver.find_element_by_xpath("//div[@id='viewmenu']/ul/li[2]/a").click()
            installed_BTN = driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(2) > a")
            installed_BTN.click()
            time.sleep(15)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/Plugin_installed-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("=== Installed Plugin Error === %s", e)
            return 0
        finally:
            pass


    #######已安装，点击+ #########
    def morePlugin(self, driver):
        time.sleep(2)
        logging.info('===Try More Plugin===')
        time.sleep(2)
        try:
            logging.info('Click + ')
            driver.find_element_by_class_name("plugins-allapp-img").click()
            logging.info("check jump all app")
            geturl = driver.current_url
            logging.info(geturl.split('/')[4])
            if geturl.split('/')[4] == 'allapp':
                logging.info("==== More Plugin Success ====")
                return 1
            else:
                logging.info("==== More Plugin Fail ====")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/morePluginError-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== More Plugin Error === %s", e)
            return 0
        finally:
            pass


    def uninstallPlugin(self, driver,unChoose):
        time.sleep(2)
        logging.info('=== Try Uninstall Plugin ===')
        try:

            driver.find_element_by_css_selector("#map > div:nth-child(2) > div.plugins-f > img.plugins-img").click()
            time.sleep(5)
            logging.info('Click uninstall')
            driver.find_element_by_css_selector("#plugin_detail > form > div > div.plugin-info > div.plugin-info-content > div > div").click()
            time.sleep(5)
            if unChoose ==1:
                logging.info('Click Sure')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
                time.sleep(15)
                return 1
            if unChoose ==2:
                logging.info('Click Cancel')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel").click()
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/uninstallPluginError-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Uninstall Plugin Error === %s", e)
            return 0
        finally:
            pass


    def check_path(self):
        time.sleep(2)


    ####检查默认APP####
    def check_defaultapp(self, driver):
        time.sleep(2)
        try:
            logging.info("=== Check Default APP ===")
            getapp = driver.find_element_by_css_selector("#map > div:nth-child(1) > div > div > p.plugins-title").text
            logging.info(getapp)
            if getapp =='Samba':
                return 1
            else:
                return 2
        except:
            return 0
        finally:
            pass


