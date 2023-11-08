# -*- coding: utf-8 -*-
import sys
import logging
import configparser
import paramiko
import time
import re
import os
import time
from selenium import webdriver
from selenium .webdriver.common.action_chains import ActionChains

class wifi:
    ###修改SSID###
    def setSSID(self,driver, choose,SSID):
        time.sleep(2)
        logging.info("=== SET SSID ===")
        try:
            ###2.4G###
            if choose == 1:
                logging.info('SET ra0 SSID')
                driver.find_element_by_id('ra0_ssid').clear()
                driver.find_element_by_id('ra0_ssid').send_keys(SSID)
            ###5G###
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                logging.info('SET rai0 SSID')
                driver.find_element_by_id("rai0_ssid").clear()
                driver.find_element_by_id("rai0_ssid").send_keys(SSID)
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                logging.info('SET guest SSID')
                driver.find_element_by_id('visitor_ssid').clear()
                driver.find_element_by_id('visitor_ssid').send_keys(SSID)
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/WiFiSSIDset-%s.jpg" %time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.info('=== Try Change SSID error===%s' % e)
            return 0
        finally:
            pass


    ###获取SSID###
    def getSSID(self, driver, choose, SSID):
        time.sleep(2)
        try:
            logging.info("=== GET SSID ===")
            if choose == 1:
                logging.info('get ra0')
                js24 = "return document.getElementById('ra0_ssid').value;"
                get24ssid = driver.execute_script(js24)
                logging.info('GET ra0 = %s' % get24ssid)
                if get24ssid == SSID:
                    return 1
                else:
                    logging.info('GET guest %s != %s' % (get24ssid, SSID))
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('get rai0')
                js5 = "return document.getElementById('rai0_ssid').value;"
                get5ssid = driver.execute_script(js5)
                logging.info('GET rai0 = %s' % get5ssid)
                if get5ssid == SSID:
                    return 2
                else:
                    logging.info('GET guest %s != %s' % (get5ssid, SSID))
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('get guest')
                jsg = "return document.getElementById('visitor_ssid').value;"
                getgssid = driver.execute_script(jsg)
                logging.info('GET guest = %s' % getgssid)
                if getgssid == SSID:
                    return 3
                else:
                    logging.info('GET guest %s != %s' % (getgssid, SSID))
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/WiFiSSIDset-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== Get SSID error===%s' % e)
            return 0
        finally:
            pass


    ###设置WiFi密码
    def setWP(self, driver, choose, pw):
        time.sleep(2)
        logging.info("=== Try SET WiFi Password ===")
        try:
            if choose == 1:
                logging.info("Set ra0 Password")
                driver.find_element_by_css_selector("#section-pane-ra0 > div:nth-child(3) > div > div.password-form > div.password-eye").click()
                time.sleep(1)
                driver.find_element_by_id('ra0_password').clear()
                driver.find_element_by_id("ra0_password").send_keys(pw)
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("Set rai0 Password")
                driver.find_element_by_css_selector("#section-pane-rai0 > div:nth-child(3) > div > div.password-form > div.password-eye").click()
                time.sleep(1)
                driver.find_element_by_id('rai0_password').clear()
                driver.find_element_by_id("rai0_password").send_keys(pw)
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('Set guest Password')
                # driver.find_element_by_css_selector("#section-pane-visitor > div:nth-child(2) > div > div.password-form > div.password-eye").click()
                driver.find_element_by_xpath("//*[@id='section-pane-visitor']/div[2]/div/div[1]/div[2]").click()
                time.sleep(1)
                driver.find_element_by_id("visitor_password").clear()
                driver.find_element_by_id('visitor_password').send_keys(pw)
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/WiFiPWset-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== SET WIFI PASSWORD ERROR === %s' % e)
            return 0
        finally:
            pass


    ####获取WiFi密码#####
    def getWP(self, driver, choose, pw):
        time.sleep(2)
        logging.info("=== GET WIFI PASSWORD ===")
        try:
            if choose == 1:
                driver.find_element_by_css_selector("#section-pane-ra0 > div:nth-child(3) > div > div.password-form > div.password-eye").click()
                time.sleep(1)
                js24 = "return document.getElementById('ra0_password').value;"
                getpw24 = driver.execute_script(js24)
                logging.info("get ra0 Password = %s" % getpw24)
                if getpw24 == pw:
                    return 1
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                driver.find_element_by_css_selector("#section-pane-rai0 > div:nth-child(3) > div > div.password-form > div.password-eye").click()
                time.sleep(1)
                js5 = "return document.getElementById('rai0_password').value;"
                getpw5 = driver.execute_script(js5)
                logging.info("get rai0 Password = %s" % getpw5)
                if getpw5 == pw:
                    return 2
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('click eye')
                # driver.find_element_by_css_selector("#section-pane-visitor > div:nth-child(3) > div > div.password-form > div.password-eye").click()
                driver.find_element_by_xpath("//*[@id='section-pane-visitor']/div[2]/div/div[1]/div[2]").click()
                time.sleep(1)
                jsg = "return document.getElementById('visitor_password').value;"
                getpwg = driver.execute_script(jsg)
                logging.info("get guest Password = %s" % getpwg)
                if getpwg == pw:
                    return 3
            time.sleep(3)
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/WiFiPWget-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== GET WIFI PASSWORD ERROR ===%s' % e)
            return 0
        finally:
            pass


    ###获取隐藏ssid状态###
    def getHide(self, driver, choose):
        time.sleep(2)
        logging.info("=== GET WIFI Hide status ===")
        try:
            if choose ==1:
                getHide24 = driver.find_element_by_id('ra0_hidessid').get_attribute('values')
                time.sleep(2)
                logging.info('getHide24 = %s' % getHide24)
                if getHide24 =='0':
                    logging.info('===ra0 Hide ===NO')
                    return 1
                if getHide24 == '1':
                    logging.info('=== ra0 Hide ===YES')
                    return 2
            if choose ==2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                getHide5 = driver.find_element_by_id('rai0_hidessid').get_attribute('values')
                time.sleep(2)
                logging.info('getHide5 = %s' % getHide5)
                if getHide5 == '0':
                    logging.info('=== rai0 Hide ===NO')
                    return 3
                if getHide5 == '1':
                    logging.info('=== rai0 Hide ===YES')
                    return 4
            logging.info('=== GET WIFI Hide Success ===')
        except Exception as e:
            driver.get_screenshot_as_file(
                os.path.dirname(os.getcwd()) + "/errorpng/WiFiHideGet-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== GET WIFI HIDE ERROR ===%s' % e)
            return 0
        finally:
            pass

    ####设置隐藏SSID####
    def setHide(self, driver, choose):
        time.sleep(2)
        logging.info("=== SET WIFI Hide status ===")
        try:
            if choose ==1 :
                driver.find_element_by_id('ra0_hidessid').click()
                time.sleep(2)
            if choose ==2 :
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                driver.find_element_by_id('rai0_hidessid').click()
                time.sleep(2)
        except Exception as e:
            driver.get_screenshot_as_file(
                os.path.dirname(os.getcwd()) + "/errorpng/WiFiHideSet-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== SET WIFI HIDE ERROR ===%s' % e)
            return 0
        finally:
            pass

    #### 高级设置 ###
    def advance(self, driver, choose):
        time.sleep(2)
        try:
            logging.info('=== Click Advance ===')
            ###2.4G###
            if choose == 1:
                logging.info('Click ra0 Advanced Setup')
                driver.find_element_by_id("ra0___advance").click()
                time.sleep(2)
            ###5G###
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('Click rai0 Advanced Setup')
                driver.find_element_by_id("rai0___advance").click()
                time.sleep(2)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/WiFiAdvance-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('===Click Advance Fail ===%s' % e)
            return 0
        finally:
            pass


    ####修改加密类型####
    def setEncryption(self, driver, choose, types):
        time.sleep(2)
        try:
            ###2.4G###
            if choose == 1:
                time.sleep(1)
                logging.info('=== Try ra0 change encipherment ===')
                driver.find_element_by_class_name('listra0').click()
                time.sleep(3)
                if types == 1:
                    logging.info('ra0none')
                    driver.find_element_by_id('ra0none').click()
                if types == 2:
                    logging.info('ra0psk2')
                    driver.find_element_by_id('ra0psk2').click()
                if types == 3:
                    logging.info('ra0psk+psk2')
                    driver.find_element_by_id('ra0psk+psk2').click()
            ###5G###
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                time.sleep(1)
                logging.info('=== Try rai0 change encipherment ===')
                driver.find_element_by_class_name('listrai0').click()
                time.sleep(3)
                if types == 1:
                    logging.info('rai0none')
                    driver.find_element_by_id('rai0none').click()
                if types == 2:
                    logging.info('rai0psk2')
                    driver.find_element_by_id('rai0psk2').click()
                if types == 3:
                    logging.info('rai0psk+psk2')
                    driver.find_element_by_id('rai0psk+psk2').click()
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('Click guest Advanced Setup')
                driver.find_element_by_class_name("listvisitor").click()
                time.sleep(3)
                if types == 1:
                    logging.info('guest none')
                    driver.find_element_by_id("visitornone").click()
                if types == 2:
                    logging.info('guest psk2')
                    driver.find_element_by_id("visitorpsk2").click()
                if types == 3:
                    logging.info('guest psk+psk2')
                    driver.find_element_by_id("visitorpsk+psk2").click()
            time.sleep(2)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/WiFiEncryption-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Change Encryption Fail ===%s' % e)
            return 0
        finally:
            pass


    ###获取加密方式
    def getEncryption(self, driver, choose):
        time.sleep(2)
        try:
            if choose == 1:
                getEncryption24 = driver.find_element_by_id('ra0_encryption').get_attribute('values')
                logging.info("%s" % getEncryption24)
                if getEncryption24 == 'psk+psk2':
                    return 1
                if getEncryption24 == 'psk2':
                    return 2
                if getEncryption24 == 'none':
                    return 3
            if choose ==2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                getEncryption5 = driver.find_element_by_id('rai0_encryption').get_attribute('values')
                logging.info("%s" % getEncryption5)
                if getEncryption5 == 'psk+psk2':
                    return 1
                if getEncryption5 == 'psk2':
                    return 2
                if getEncryption5 == 'none':
                    return 3
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                getEncryptionGuest = driver.find_element_by_id('visitor_encryption').get_attribute('values')
                logging.info("%s" % getEncryptionGuest)
                if getEncryptionGuest == 'psk+psk2':
                    return 1
                if getEncryptionGuest == 'psk2':
                    return 2
                if getEncryptionGuest == 'none':
                    return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/WiFiEncryption-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Change Encryption Fail ===%s' % e)
            return 0
        finally:
            pass

    ###设置信道###
    def setChannel(self, driver, choose):
        logging.info("=== Set Channel ===")
        time.sleep(2)
        try:
            if choose == 1:
                logging.info("=== Set ra0 Channel ===")

            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("=== Set rai0 Channel ===")

        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/ChannelSet-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Set Channel Fail ===%s' % e)
            return 0
        finally:
            pass


    ###获取信道###
    def getChannel(self, driver, choose):
        logging.info("=== Get Channel ===")
        time.sleep(2)
        try:
            if choose == 1:
                logging.info("=== Get ra0 Channel ===")

            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("=== Get rai0 Channel ===")
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/ChannelGet-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Get Channel Fail ===%s' % e)
            return 0
        finally:
            pass


    ###设置HT模式###
    def setHT(self, driver, choose, types):
        logging.info("=== Set HT ===")
        time.sleep(3)
        try:
            if choose == 1:
                logging.info("=== Set ra0 HT ===")
                #driver.find_element_by_id("ra0_htmode").click()
                #driver.find_element_by_class_name("listra0").click()
                driver.find_element_by_css_selector("#ra0_htmode > #dropdownMenu1").click()
                time.sleep(3)
                if types == 1:
                    #driver.find_element_by_id("ra00").click()
                    driver.find_element_by_xpath("(//span[@id='ra00'])[2]").click()
                if types == 2:
                    #driver.find_element_by_id("ra01").click()
                    driver.find_element_by_xpath("(//span[@id='ra01'])[2]").click()
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("=== Set rai0 HT ===")
                #driver.find_element_by_id("rai0_htmode").click()
                driver.find_element_by_css_selector("#rai0_htmode > #dropdownMenu1").click()
                time.sleep(3)
                if types == 3:
                    # driver.find_element_by_id("rai00").click()
                    driver.find_element_by_xpath("(//span[@id='rai00'])[2]").click()
                if types == 4:
                    driver.find_element_by_id("rai01").click()
                    #driver.find_element_by_xpath("(//span[@id='rai01'])[2]").click()
                if types == 5:
                    driver.find_element_by_id("rai02").click()
                    #driver.find_element_by_xpath("(//span[@id='rai02'])[2]").click()
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/HTSet-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== Set HT Fail ===%s' % e)
            return 0
        finally:
            pass


    def getHT(self, driver, choose):
        logging.info("=== Get HT ===")
        time.sleep(2)
        try:
            if choose == 1:
                logging.info("=== Get ra0 HT ===")
                getHT24 = driver.find_element_by_id("ra0_htmode").get_attribute('values')
                logging.info('get ra0 HT = %s' % getHT24)
                if getHT24 == '0':
                    logging.info('HT = 20/40')
                    return 1
                if getHT24 == '1':
                    logging.info('HT = 40')
                    return 2
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("=== Get rai0 HT ===")
                getHT5 = driver.find_element_by_id("rai0_htmode").get_attribute('values')
                logging.info('get rai0 HT = %s' % getHT5)
                if getHT5 == '0':
                    logging.info('HT = 20/40')
                    return 3
                if getHT5 == '1':
                    logging.info('HT = 40')
                    return 4
                if getHT5 == '2':
                    logging.info('HT = 80')
                    return 5
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/HTGet-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning('=== Get HT Fail ===%s' % e)
            return 0
        finally:
            pass


    ####点击WiFi按钮
    def clickWiFi(self, driver, choose):
        time.sleep(2)
        try:
            if choose == 1:
                logging.info("Click ra0 BTN")
                driver.find_element_by_id('section_switch_ra0').click()
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("Click rai0 BTN")
                driver.find_element_by_id("section_switch_rai0").click()
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('Click guest BTN')
                driver.find_element_by_id("section_switch_visitor").click()
            time.sleep(5)
            try:
                logging.info('Sure')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").is_displayed()
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            except:
                pass
            time.sleep(15)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/error/WiFiClick-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Change Encryption Fail ===%s' % e)
            return 0
        finally:
            pass


    ###获取WiFi
    def getWiFi(self,driver, choose):
        time.sleep(2)
        try:
            logging.info("===GET WIFI Status===")
            if choose ==1:
                get24 = driver.find_element_by_css_selector("#section_wireless_ra0 > div > div.dummy-panel-close.display-none > div > p").text
                time.sleep(1)
                if get24 == '2.4G网络未开启':
                    return 1
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                get5 = driver.find_element_by_css_selector("#section_wireless_rai0 > div > div.dummy-panel-close.display-none > div > p").text
                if get5 == '5G网络未开启':
                    return 2
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                getg = driver.find_element_by_css_selector("#section_wireless_visitor > div > div.dummy-panel-close > div > p").text
                if getg =='访客网络未开启':
                    return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/error/WiFiGET-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Change Encryption Fail ===%s' % e)
            return 0
        finally:
            pass


    ####保存按钮#####
    def savewifi(self, driver, choose):
        time.sleep(2)
        logging.info("=== Save WiFi ===")
        try:
            if choose == 1:
                logging.info("Save rao")
                driver.find_element_by_id("btn_ra0").click()
            if choose == 2:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info("Save rai0")
                driver.find_element_by_id("btn_rai0").click()
            if choose == 3:
                js_ = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js_)
                time.sleep(1)
                logging.info('Save guest')
                driver.find_element_by_id("btn_visitor").click()
            time.sleep(5)
            try:
                logging.info('Sure')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").is_displayed()
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            except:
                pass
            time.sleep(15)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/error/WiFiSave-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('=== Save WiFi ERROR === %s' % e)
            return 0
        finally:
            pass
