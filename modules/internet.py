# -*- coding:utf-8 -*-
import time
import logging
import configparser
import paramiko
import json
import time
import re
import os
import sys
from selenium .webdriver.common.action_chains import ActionChains

class internet:
    def __call__(self,ipaddr, netmask, gateway, dns1, dns2):
        ipaddr = ipaddr
        netmask = netmask
        gateway = gateway
        dns1 = dns1
        dns2 = dns2


    ####选择进入某页面进行设置####
    def setup_choose(self, driver, choose):
        time.sleep(2)
        try:
            logging.info("try enter router setup")
            driver.find_element_by_link_text(u"路由设置").click()
            time.sleep(5)
            if choose == 1:
                logging.info("try click wifi setup ")
                driver.find_element_by_link_text(u"WIFI设置").click()
                time.sleep(2)
                return 1
            if choose == 2:
                logging.info("try click internet steup ")
                driver.find_element_by_link_text(u"互联网设置").click()
                time.sleep(2)
                return 2
            if choose == 3:
                logging.info("try click wireless repeater setup ")
                driver.find_element_by_link_text(u"无线中继").click()
                return 3
            if choose == 4:
                logging.info("try click LAN setup")
                driver.find_element_by_link_text(u"局域网设置").click()
                return 4
            if choose == 5:
                logging.info("try click system setup ")
                driver.find_element_by_link_text(u"系统设置").click()
                return 5
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/setup_choose-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== enter router setup error === %s", e)
            return 0
        finally:
            pass


    ###设置静态IP###
    def set_statics(self, driver, test_statics, ipaddr, netmask, gateway, dns1, dns2):
        logging.info('Try SET Static')
        time.sleep(2)
        try:
            driver.find_element_by_id("dropdownMenu1").click()
            time.sleep(2)
            ###静态IP元素定位###
            set_internetstatic = driver.find_element_by_id("set_internetstatic")
            ActionChains(driver).click(set_internetstatic).perform()
            time.sleep(2)
            logging.info("set static ip")
            driver.find_element_by_id("set_internet_ipaddr").clear()
            driver.find_element_by_id("set_internet_ipaddr").send_keys(ipaddr)
            logging.info("set static gateway")
            driver.find_element_by_id("set_internet_gateway").clear()
            driver.find_element_by_id("set_internet_gateway").send_keys(gateway)
            if test_statics == 1:
                logging.info("test static fill")
            else:
                logging.info("test full set static")
                driver.find_element_by_id("set_internet_netmask").clear()
                driver.find_element_by_id("set_internet_netmask").send_keys(netmask)
                time.sleep(1)
                driver.find_element_by_id("set_internet_dns1").clear()
                driver.find_element_by_id("set_internet_dns1").send_keys(dns1)
                time.sleep(1)
                driver.find_element_by_id("set_internet_dns2").clear()
                driver.find_element_by_id("set_internet_dns2").send_keys(dns2)
                time.sleep(1)
            time.sleep(1)
            driver.find_element_by_id("btn_staticButton").click()
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/div/div[2]").click()
            time.sleep(1)
            logging.info('SET Static Success')
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/set_statics-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Set Static error==== %s' %e)
            return 0
        finally:
            pass


    ###获取静态IP设置###
    def get_static(self, driver):
        time.sleep(1)
        try:
            get_ipaddr = "return document.getElementById('set_internet_ipaddr').value;"
            get_ipaddrs=driver.execute_script(get_ipaddr)
            logging.info('Get static IP = %s' % get_ipaddrs)

            get_netmask = "return document.getElementById('set_internet_netmask').value;"
            get_netmasks=driver.execute_script(get_netmask)
            logging.info('Get static NETMASK = %s' % get_netmasks)

            get_gateway = "return document.getElementById('set_internet_gateway').value;"
            get_gateways = driver.execute_script(get_gateway)
            logging.info('Get static Gateway = %s' % get_gateways)


            get_dns1 = "return document.getElementById('set_internet_dns1').value;"
            get_dns1s = driver.execute_script(get_dns1)
            logging.info('Get static DNS1 = %s' % get_dns1s)

            get_dns2 = "return document.getElementById('set_internet_dns2').value;"
            get_dns2s = driver.execute_script(get_dns2)
            logging.info('Get static DNS2 = %s' % get_dns2s)
            result = 0

            if get_ipaddrs == ipaddr:
                logging.info(' %s = %s ' % (get_ipaddrs, ipaddr))
                result = result + 1

            if get_netmasks == netmask:
                logging.info('')
                result = result + 1
            if get_gateways == gateway:
                logging.info('%s = %s' % (get_gateway, gateway))
                result = result + 1
            if get_dns1s == dns1:
                logging.info('%s = %s ' % (get_dns1s, dns1))
                result = result + 1
            if get_dns2s == dns2:
                logging.info('%s = %s ' % (get_dns2s,dns2))
                result = result + 1
            return result
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/GetStatic-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('==== GET Static error ==== %s' %e)
            return 0