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
#from tools import *
from selenium .webdriver.common.action_chains import ActionChains

class router_setup:
    def __call__(self, ra0ssid, rai0ssid, wanmac, default_ip, default_pw):
        self.ra0ssid = ra0ssid
        self.rai0ssid = rai0ssid
        self.wanmac = wanmac


    ####选择进入某页面进行设置####
    def setup_choose(self, driver, choose):
        time.sleep(2)
        try:
            logging.info("try enter router setup")
            driver.find_element_by_css_selector("#mainmenu > ul > li:nth-child(4) > a > span").click()
            time.sleep(12)
            if choose == 1:
                logging.info("click wifi setup ")
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(1) > a").click()
                time.sleep(2)
                return 1
            if choose == 2:
                logging.info("click internet steup ")
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(2) > a").click()
                time.sleep(2)
                return 2
            if choose == 3:
                logging.info("click wireless repeater setup ")
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(3) > a").click()
                return 3
            if choose == 4:
                logging.info("click LAN setup")
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(4) > a").click()
                return 4
            if choose == 5:
                logging.info("click system setup ")
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(5) > a > span").click()
                return 5
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/setup_choose-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== enter router setup error === %s", e)
            return 0
        finally:
            pass


    #####修改路由网关#####
    def setGateway(self, driver, newGateway, setGatewayChoose):
        logging.info('Try Modify Gateway')
        time.sleep(2)
        try:
            logging.info('input new gateway')
            driver.find_element_by_id("network_lan_lan_ip").clear()
            driver.find_element_by_id("network_lan_lan_ip").send_keys(newGateway)
            logging.info("modify gateway %s" % newGateway)
            time.sleep(1)
            logging.info('click modify gateway btn')
            driver.find_element_by_id("btn_lanipButton").click()
            time.sleep(2)
            if setGatewayChoose == 1:
                logging.info('=== Click Sure ===')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
                logging.info('restart router wait 90s')
                time.sleep(90)
                logging.info('wait ok')
                return 1
            if setGatewayChoose == 2:
                logging.info('=== Click Cancel ===')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel").click()
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/ModifyGateway-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Modify Gateway error === %s", e)
            return 0
        finally:
            pass


    #####################
    # 获取网关
    #####################
    def getGateway(self,driver,default_ip,newGateway):
        time.sleep(2)
        logging.info('===Try Get Gateway===')
        time.sleep(2)
        try:
            js = "return document.getElementById('network_lan_lan_ip').value;"
            getGateway=driver.execute_script(js)
            if getGateway == default_ip:
                logging.info("getGateway(%s) == default(%s)" % (getGateway, default_ip))
                return 1
            if getGateway == newGateway:
                logging.info("getGateway(%s) == newGateway(%s)" % (getGateway, newGateway))
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/GetGatewayError-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Get Gateway Error === %s", e)
            return 0
        finally:
            pass


    ###DHCP服务,局域网设置###
    def dhcpServer(self, driver,dhcpServerChoose):
        logging.info('Try Click DHCP Server')
        time.sleep(2)
        try:
            driver.find_element_by_id("network_dhcp_dhcpService").click()
            time.sleep(5)
            if dhcpServerChoose == 1:
                logging.info('Click Sure')
                driver.find_element_by_css_selector('body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure').click()
                return 1
            if dhcpServerChoose == 2:
                logging.info('Click Cancel')
                driver.find_element_by_css_selector('body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel').click()
                return 2
            time.sleep(12)
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/DHCPServerError-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== DHCP Server error === %s", e)
            return 0
        finally:
            pass



    ###获取wifi配置###
    def getwifi(self, driver, default_24ssid, default_5ssid, default_passward):
        logging.info('Try Get WiFi')
        router_setup.iwconfig_ssid(self)
        time.sleep(2)
        try:
            ###获取ssid和密码###
            js = "return document.getElementById('ra0_ssid').value;"
            ssid24=driver.execute_script(js)
            if ssid24 == default_24ssid:
                if 'ra0='+ssid24 == self.ra0ssid:
                    logging.info("web_24ssid=%s %s" % (ssid24,self.ra0ssid))
                else:
                    logging.error("web_24ssid != iwconfig_24ssid")
            else:
                logging.warning("===test fail 24 ssid===")
            js = "return document.getElementById('ra0_password').value;"
            passward24=driver.execute_script(js)
            if passward24 == default_passward:
                pass
            else:
                logging.warning("===test fail 24 passward===")
            js = "return document.getElementById('rai0_ssid').value;"
            ssid5=driver.execute_script(js)
            if ssid5 == default_5ssid:
                if 'rai0='+ssid5 == self.rai0ssid:
                    logging.info("web_5ssid=%s %s" % (ssid5, self.rai0ssid))
                else:
                    logging.error("web_5ssid != iwconfig_5ssid")
            else:
                logging.warning("===test fail 5 ssid===")
            js = "return document.getElementById('rai0_password').value;"
            passward5=driver.execute_script(js)
            if passward5 == default_passward:
                pass
            else:
                logging.warning("===test fail 5 passward===")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/GetWiFi-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===get wifi info error=== %s", e)
            return 0
        finally:
            pass


    def iwconfig_ssid(self):
        config = configparser.ConfigParser()
        config.read(sys.path[2]+'\\OS3.1\\configure\\'+'testconfig.ini', encoding='UTF-8')
        default_ip = config.get('Default', 'default_ip')
        default_pw = config.get('Default', 'default_pw')
        ssid_cmd = ['iwconfig ra0', 'iwconfig rai0']
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(default_ip, 22, "root", default_pw)
        for ssid_cmd in ssid_cmd:
            print(ssid_cmd)
            stdin, stdout, stderr = ssh.exec_command(ssid_cmd)
            list = stdout.readlines()
            ssid = list[0]
            m = re.match(r'(.*):\"((.*))\"', ssid)
            if m:
                logging.info(m.group(2))
            else:
                logging.error("not match")
            if ssid_cmd == 'iwconfig ra0':
                self.ra0ssid = 'ra0='+ m.group(2)
                logging.info(self.ra0ssid)
            if ssid_cmd == 'iwconfig rai0':
                self.rai0ssid = 'rai0='+ m.group(2)
                logging.info(self.rai0ssid)

    def setWan(self, driver, wanChoose):
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        logging.info("=== SET WAN Choose===")
        driver.find_element_by_id("dropdownMenu1").click()
        time.sleep(3)
        try:
            if wanChoose == 1:
                logging.info("=== SET DHCP ===")
                set_internetstatic = driver.find_element_by_id("set_internetdhcp")
                ActionChains(driver).click(set_internetstatic).perform()
                time.sleep(3)
                return 1
            if wanChoose == 2:
                logging.info('=== Set PPPoE ===')
                set_internet = driver.find_element_by_id("set_internetpppoe")
                ActionChains(driver).click(set_internet).perform()
                time.sleep(3)
                return 2
            if wanChoose == 3:
                logging.info("=== SET Static ===")
                set_internetstatic = driver.find_element_by_id("set_internetstatic")
                ActionChains(driver).click(set_internetstatic).perform()
                time.sleep(3)
                return 3
        except Exception as e:
            return 0
        finally:
            pass


    ####获取联网设置类型####
    def getwan(self, driver, pppoe_str, dhcp_str, static_str):
        logging.info('Try Get WAN')
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:
            logging.info("get wan type")
            wantype=driver.find_element_by_id("dropdownMenu1").text
            logging.info("wan type %s", wantype)
            if wantype == pppoe_str:
                logging.info('WAN=PPPoE')
                return 1
            elif wantype == dhcp_str:
                logging.info('WAN=DHCP')
                return 2
            elif wantype == static_str:
                logging.info('WAN=Static')
                return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/GetWan-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===get wan type error=== %s", e)
            return 0
        finally:
            pass


    ####设置PPPoE#####
    def setPPPoE(self, driver,ppp_choose, pppoe_user, pppoe_pw, mtu, pppoe_dns):
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:
            logging.info('=== try Set PPPoE ===')
            driver.find_element_by_id("dropdownMenu1").click()
            time.sleep(3)
            set_internet = driver.find_element_by_id("set_internetpppoe")
            ActionChains(driver).click(set_internet).perform()
            time.sleep(3)
            driver.find_element_by_css_selector("#set_internet_usr").clear()
            driver.find_element_by_css_selector("#set_internet_usr").send_keys(pppoe_user)
            time.sleep(1)
            driver.find_element_by_css_selector("#section-pane-set_internet > div:nth-child(4) > div > div.password-form > div.password-eye").click()
            time.sleep(1)
            driver.find_element_by_css_selector("#set_internet_pass").clear()
            driver.find_element_by_css_selector("#set_internet_pass").send_keys(pppoe_pw)
            time.sleep(5)
            if ppp_choose == 1:
                logging.info('set MTU')
                driver.find_element_by_id("set_internet_mtu").clear()
                driver.find_element_by_id("set_internet_mtu").send_keys(mtu)
            if ppp_choose == 2:
                logging.info('set MUT and DNS')
                driver.find_element_by_id("set_internet_mtu").clear()
                driver.find_element_by_id("set_internet_mtu").send_keys(mtu)
                driver.find_element_by_id("").clear()
                driver.find_element_by_id("").send_keys(pppoe_dns)
            time.sleep(1)
            driver.find_element_by_id("btn_pppoeButton").click()
            logging.info("Set pppoe success")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/setPPPoE-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Set PPPoE error==== %s' %e)
            return 0
        finally:
            pass


    ###获取PPPoE设置###
    def get_pppoes(self,driver, pppoe_user, pppoe_pw, mtu, pppoe_dns):
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:
            pppusr = "return document.getElementById('set_internet_usr').value;"
            get_pppusrs = driver.execute_script(pppusr)
            logging.info('Get PPPoE usre = %s' % get_pppusrs)

            get_ppppass = "return document.getElementById('set_internet_pass').value;"
            get_ppppasss = driver.execute_script(get_ppppass)
            logging.info('Get PPPoE password = %s' % get_ppppasss)

            get_pppmtu = "return document.getElementById('set_internet_mtu').value;"
            get_pppmtus = driver.execute_script(get_pppmtu)
            logging.info('Get PPPoE password = %s' % get_pppmtus)

            get_pppdns = "return document.getElementById('set_internet_DNS_pppoe').value;"
            get_pppdnss = driver.execute_script(get_pppdns)
            logging.info('Get PPPoE password = %s' % get_pppdnss)

            # get_pppdns = "return document.getElementById('set_internet_pppoe_status').value;"
            # get_pppdnss = driver.execute_script(get_pppdns)
            # logging.info('Get PPPoE password = %s' % get_pppdnss)

            get_pppoe_result = 0
            if get_pppusrs == pppoe_user:
                logging.info('%s = %s' % (get_pppusrs,pppoe_user))
                get_pppoe_result = get_pppoe_result + 1
            else:
                logging.warning('%s != %s' % (get_pppusrs,pppoe_user))
            if get_ppppasss == pppoe_pw:
                logging.info('%s = %s' % (get_ppppasss,pppoe_pw))
                get_pppoe_result = get_pppoe_result + 1
            else:
                logging.warning('%s != %s' % (get_ppppasss,pppoe_pw))
            if get_pppmtus == mtu:
                logging.info('%s = %s' % (get_pppmtus,mtu))
                get_pppoe_result = get_pppoe_result + 1
            else:
                logging.warning('%s != %s' % (get_pppmtus,mtu))
            if get_pppdnss == pppoe_dns:
                logging.info('%s = %s' % (get_pppdnss,pppoe_dns))
                get_pppoe_result = get_pppoe_result + 1
            else:
                logging.warning('%s != %s' % (get_pppdnss,pppoe_dns))

            logging.info('%s' % get_pppoe_result)
            return get_pppoe_result
            #### 返回4为成功 ####
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/getPPPoE-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Get PPPoE error==== %s' %e)
            return 0
        finally:
            pass


    ###获取默认PPPOE MTU###
    def get_mtu(self, driver):
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:
            logging.info('Get default MTU')
            get_pppmtu = "return document.getElementById('set_internet_mtu').value;"
            get_pppmtus = driver.execute_script(get_pppmtu)
            logging.info('Get PPPoE password = %s' % get_pppmtus)
            if get_pppmtus == '1492':
                return 1
            else:
                driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/getMTUfail-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
                logging.warning('get_pppmtus(%s) != 1492' % (get_pppmtus))
                return 0
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/getMTUerror-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Get PPPoE error==== %s' %e)
            return 0
        finally:
            pass


    ###设置DHCP DNS1\DNS2###
    def setDHCP(self, driver, dhcpChoose,dns3, dns4):
        logging.info('Try Set DHCP')
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:
            driver.find_element_by_id("dropdownMenu1").click()
            time.sleep(2)
            ###DHCP元素定位###
            logging.info("try click DHCP")
            set_internetstatic = driver.find_element_by_id("set_internetdhcp")
            ActionChains(driver).click(set_internetstatic).perform()
            time.sleep(2)
            if dhcpChoose == 1:
                logging.info("===select Manual DNS===")
                driver.find_element_by_css_selector("#set_internet_radiobox > div.second-radio > input[type='radio']").click()
                driver.find_element_by_id("set_internet_dns3").clear()
                driver.find_element_by_id("set_internet_dns3").send_keys(dns3)
                driver.find_element_by_id("set_internet_dns4").clear()
                driver.find_element_by_id("set_internet_dns4").send_keys(dns4)
            if dhcpChoose == 2:
                logging.info('===select Auto DNS====')
                driver.find_element_by_css_selector("#set_internet_radiobox > div.first-radio > input[type='radio']").click()
            time.sleep(2)
            driver.find_element_by_id("btn_dhcpButton").click()
            time.sleep(1)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            time.sleep(10)
            logging.info('SET DHCP Success')
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/setDHCP-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Set DHCP DNS error==== %s' % e)
            return 0
        finally:
            pass


    ###获取DHCP DNS1/DNS2###
    def getDHCP(self,driver,dns3, dns4):
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:
            get_dns3 = "return document.getElementById('set_internet_dns3').value;"
            get_dns3s = driver.execute_script(get_dns3)
            logging.info('Get DHCP DNS1 = %s' % get_dns3s)
            print(type(get_dns3))
            get_dns4 = "return document.getElementById('set_internet_dns4').value;"
            get_dns4s = driver.execute_script(get_dns4)
            logging.info('Get DHCP DNS2 = %s' % get_dns4s)
            if get_dns3s == dns3 and get_dns4s == dns4:
                logging.info('%s = %s ' % (get_dns3s, dns3))
                logging.info('%s = %s ' % (get_dns4s, dns4))
                return 1
            else:
            # if get_dns3 == None and get_dns4 == None:
                logging.info('=== DNS1/DNS2 NONE===')
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/getDHCP-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('===get DHCP DNS error==== %s' % e)
            driver.quit()
            return 0
        finally:
            pass


    ###设置静态IP###
    def set_statics(self, driver, test_statics, ipaddr, netmask, gateway, dns1, dns2):
        logging.info('Try SET Static')
        time.sleep(2)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        try:

            driver.find_element_by_id("dropdownMenu1").click()
            time.sleep(2)
            ###静态IP元素定位###
            logging.info('SET Static')
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
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            time.sleep(10)
            logging.info('SET Static Success')
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/set_statics-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Set Static error==== %s' %e)
            return 0
        finally:
            pass


    #####################
    # 获取静态IP设置
    #####################
    def get_static(self, driver, ipaddr, netmask, gateway, dns1, dns2):
        logging.info('======GET static ip ====')
        time.sleep(1)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
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
            else:
                logging.info(' %s != %s ' % (get_ipaddrs, ipaddr))

            if get_netmasks == netmask:
                logging.info('%s = %s' % (get_netmasks, netmask))
                result = result + 1
            else:
                logging.info('%s != %s' % (get_netmasks, netmask))

            if get_gateways == gateway:
                logging.info('%s = %s' % (get_gateways, gateway))
                result = result + 1
            else:
                logging.info('%s != %s' % (get_gateways, gateway))

            if get_dns1s == dns1:
                logging.info('%s = %s ' % (get_dns1s, dns1))
                result = result + 1
            else:
                 logging.info('%s != %s ' % (get_dns1s, dns1))

            if get_dns2s == dns2:
                logging.info('%s = %s ' % (get_dns2s, dns2))
                result = result + 1
            else:
                logging.info('%s != %s ' % (get_dns2s, dns2))

            logging.info('result = %s' % result)
            return result
            ### result=5时，为成功###
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/GetStatic-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('==== GET Static error ==== %s' %e)
            return 0
        finally:
            pass


    ###mac克隆###
    def macclone(self, driver, macChoose, testMac):
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        logging.info("=== try set mac clone ===")
        time.sleep(5)
        try:
            logging.info('GET Terminal Mac')
            ####进入手动输入MAC地址
            if macChoose == 1:
                logging.info('=== Try Set Mac Clone Text===')
                driver.find_element_by_id("clone-mac_macaddr").clear()
                driver.find_element_by_id("clone-mac_macaddr").send_keys(testMac)
            # 调用js
            driver.find_element_by_id("btn_mac_clone").click()
            time.sleep(5)
            js = "return document.getElementById('clone-mac_macaddr').value;"
            now_mac = driver.execute_script(js)
            logging.info('Now_Mac= %s' % now_mac)
            clone_mac = driver.find_element_by_id("clone_mac_label").text
            logging.info('clone mac = %s' % clone_mac)
            if now_mac == clone_mac:
                logging.info('%s = %s' % (now_mac, clone_mac))
                logging.info("=== set mac clone success ===")
                return 1
            else:
                logging.info('%s != %s' % (now_mac, clone_mac))
                logging.warning("=== Set Mac Clone Fail ===")
                errorinfo=driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > p").text
                logging.info(errorinfo)
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div").click()
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/MacClone-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('=== error try set mac clone === %s' % e)
            return 0
        finally:
            pass


    ####################
    ###获取WAN MAC###
    ####################
    def getwanmac(self, driver, wan_mac):
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        logging.info('=== Try GET WAN MAC ===')
        router_setup.network_wan(self)
        time.sleep(2)
        try:
            ###获取wanmac###
            new_mac = driver.find_element_by_id("clone_mac_label").text
            if new_mac == wan_mac:
                if new_mac == self.mac:
                    logging.info("web_mac=%s %s" % (new_mac, self.x))
                    return 1
                else:
                    logging.error("===web_mac != network_mac===")
            else:
                logging.warning("===test fail wan mac===")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/getwanmac-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Get Wan MAC Fail==== %s' % e)
            return 0
        finally:
            pass


    ###########################
    ###获取Network WAN MAC###
    ###########################
    def network_wan(self, default_ip, default_pw):
        logging.info('SSH get WAN mac')
        mac_cmd = 'uci show network.wan'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(default_ip, 22, "root", default_pw)
        print( mac_cmd)
        stdin, stdout, stderr = ssh.exec_command(mac_cmd)
        list = stdout.readlines()
        mac = list[3]
        wanmac = re.match(r'(.*)=(.*)', mac)
        if wanmac:
            logging.info(wanmac.group(2))
            self.wanmac =  wanmac.group(2)
            #print(m.group(2))
        else:
            logging.error("not match")


    ####################
    ###恢复MAC克隆###
    ####################
    def restore_mac(self, driver):
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        logging.info("=== Try Restore Mac ===")
        time.sleep(2)
        try:
            logging.info('click mac recovery btn')
            driver.find_element_by_id("btn_mac_recovery").click()
            logging.info('click success')
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/restore_mac-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====Set mac clone error==== %s' %e)
            return 0
        finally:
            pass


    #####################
    # 重启路由器
    #####################
    def restart(self, driver, restart_wtime):
        logging.info("try restart")
        time.sleep(10)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        try:
            driver.find_element_by_id("btn_re_boot").click()
            time.sleep(4)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            time.sleep(restart_wtime)
            logging.info("restart success")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/restart-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error('====restart error==== %s' % e)
            return 0
        finally:
            pass


    #####################
    # 重置路由器
    #####################
    def reset(self, driver,reset_wtime):
        logging.info("=== Reset ===")
        time.sleep(10)
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        try:
            driver.find_element_by_id("btn_reset").click()
            # driver.find_element_by_id("btn_reset").click()
            time.sleep(5)
            logging.info("click reset sure")
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            logging.info("wait reset %s" % reset_wtime)
            time.sleep(reset_wtime)
            logging.info("wait reset time ok")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/reset-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Reset ERROR=== %s" % e)
            return 0
        finally:
            pass


    #####################
    # 升级固件
    #####################
    def upgrade(self, driver, new_build, upgrade_wtime):
        time.sleep(15)
        try:
            logging.info("try upgrade")
            # driver.find_element_by_name("filedata").clear()
            driver.find_element_by_name("filedata").send_keys(new_build)
            #driver.find_element_by_css_selector("#upgrade_upload_local > form > input.cbi-input-file").clear()
            # driver.find_element_by_css_selector("#upgrade_upload_local > form > input.cbi-input-file").send_keys(new_build)
            logging.info('wait up file')
            time.sleep(60)
            logging.info("Get update Info")
            upInfo=driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > p").text
            logging.info(upInfo)
            if upInfo =='固件上传完成，是否升级？':
                logging.info('sure update file')
                driver.find_element_by_css_selector("div.newifi-btn.btn-sure").click()
                logging.info('wait update time %s' % upgrade_wtime)
                time.sleep(upgrade_wtime)
                return 1
            if upInfo =='固件上传失败':
                logging.info("Error Click sure")
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div").click()
                return 2
            if upInfo =='您选择的固件不是小云的官方固件，不允许进行升级。':
                logging.info("Error Click sure")
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div").click()
                return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/upgrade-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("upgrade error %s" %e)
            return 0
        finally:
            pass


    #####################
    # 修改路由器管理密码
    #####################
    def set_password(self, driver, default_pw, new_pw):
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
        time.sleep(1)
        logging.info('Try SET Password')
        time.sleep(3)
        try:
            # driver.find_element_by_id("set_pass_word_old_passwd").clear()
            # driver.find_element_by_id("set_pass_word_old_passwd").send_keys(default_pw)
            # time.sleep(1)
            # driver.find_element_by_id("set_pass_word_new_passwd").clear()
            # driver.find_element_by_id("set_pass_word_new_passwd").send_keys(new_pw)
            # time.sleep(1)
            # driver.find_element_by_id("set_pass_word_re_passwd").clear()
            # driver.find_element_by_id("set_pass_word_re_passwd").send_keys(new_pw)
            driver.find_element_by_xpath("//*[@id='section-pane-set_pass_word']/div[1]/div/div[1]/div[1]/input[2]").clear()
            driver.find_element_by_xpath("//*[@id='section-pane-set_pass_word']/div[1]/div/div[1]/div[1]/input[2]").send_keys(default_pw)
            logging.info("input default router password == %s" % default_pw)
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='section-pane-set_pass_word']/div[2]/div/div[1]/div[1]/input[2]").clear()
            driver.find_element_by_xpath("//*[@id='section-pane-set_pass_word']/div[2]/div/div[1]/div[1]/input[2]").send_keys(new_pw)
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='section-pane-set_pass_word']/div[3]/div/div[1]/div[1]/input[2]").clear()
            driver.find_element_by_xpath("//*[@id='section-pane-set_pass_word']/div[3]/div/div[1]/div[1]/input[2]").send_keys(new_pw)
            time.sleep(1)
            logging.info("input default router password == %s" % new_pw)
            driver.find_element_by_id("btn_set_pass_word").click()
            logging.info("save new password success")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/set_password-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("=== Save new password error === %s" % e)
            return 0
        finally:
            pass


    #####################
    # 下载系统日志模块代码
    #####################
    def downlog(self, driver, temp):
        logging.info('Try Down log')
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(1)
        time.sleep(4)
        try:
            logging.info("try download log")
            driver.find_element_by_id("btn_sys_log").click()
            time.sleep(10)
            downlog_result=driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > p").text
            logging.info("down log result == %s" % downlog_result)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-ready").click()
            time.sleep(5)
            logging.info("check down log file")
            checkfile = os.path.exists(temp)
            if checkfile == True:
                logging.info("down log success")
                return 1
            else:
                logging.warning("down log fail")
                return 0
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/downlog-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===down log error===%s" % e)
            return 0
        finally:
            pass


    #####################
    # 获取系统状态信息
    #####################
    def displaySystemInfo(self, driver):
        logging.info('Try get System Info')
        time.sleep(2)
        try:
            logging.info("try to display system infomation")
            driver.find_element_by_id("btn_sysinfo").click()
            time.sleep(2)
            information = driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div").text
            # print(information)
            temp = information.split()
            # print(temp)
            # 获取LAN口MAC
            lan_mac = temp[1].split(':', 1)[1]
            # 获取LAN口IP
            lan_ip = temp[2].split(':', 1)[1]
            # 获取子网掩码
            mask = temp[3].split(':', 1)[1]
            # 获取2.4G开关状态
            wifi_24 = temp[5].split(':', 1)[1]
            # 获取2.4GSSID
            wifi_24_ssid = temp[6].split(':', 1)[1]
            # 获取2.4G信道
            wifi_24_channel = temp[7].split(':', 1)[1]
            # 获取访客wifi状态
            wifi_guest = temp[8].split(':', 1)[1]
            # 获取5G开关状态
            wifi_5 = temp[9].split(':', 1)[1]
            # 获取5GSSID
            wifi_5_ssid = temp[10].split(':', 1)[1]
            # 获取5G信道
            wifi_5_channel = temp[11].split(':', 1)[1]
            # 获取WAN口类型
            wan_status = temp[13].split(':', 1)[1]
            # 获取WAN口MAC
            wan_mac = temp[14].split(':', 1)[1]
            # 获取WAN口IP
            wan_ip = temp[15].split(':', 1)[1]
            # 获取网关
            gate = temp[16].split(':', 1)[1]
            # 获取DNS
            dns = temp[17].split(':', 1)[1]
            # print(dns)
            return lan_mac, lan_ip, mask, wifi_24, wifi_24_ssid, wifi_24_channel, wifi_5, wifi_5_ssid, wifi_5_channel, wan_status, wan_mac, wan_ip, gate, dns
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/displaySystemInfo-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===display system info fail===%s" %e)
            return 0
        finally:
            pass
