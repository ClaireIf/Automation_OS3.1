# -*- coding:utf-8 -*-
###################################
#   初始化配置
###################################
import logging
import time
import os

class initialize:
    ###初始化首页###
    def homepage(self, driver):
        time.sleep(3)
        try:
            logging.info("Initialize configuration")
            driver.find_element_by_id("initalize").click()
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/homepage-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("enter initialize fail %s" % e)
            return 0
        finally:
            pass


    def homepageD1(self, driver):
        time.sleep(3)
        try:
            logging.info("===D1 Try Click Agree ===")
            driver.find_element_by_id("init-protocol-checkbox").click()
            logging.info("D1 Initialize configuration")
            driver.find_element_by_id("initalize").click()
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/homepageD1-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("enter initialize fail %s" % e)
            return 0
        finally:
            pass


    ###判断网络类型###
    def detect_wan(self, driver):
        flag = ['运营商', 'DHCP']
        try:
            tip = str(driver.find_element_by_css_selector("p.tips-text").text)
            for i in flag:
                if tip.find(i) > -1:
                    print(i)
                    if i == 'DHCP':
                        return 1
                    elif i == '运营商':
                        return 2
                    else:
                        return 3
        except Exception as e:
            logging.error("detect wan fail %s" % e)
            return 0
        finally:
            pass


    ###DHCP###
    def detection_dhcp(self, driver):
        time.sleep(3)
        try:
            logging.info('try DHCP configuration')
            time.sleep(15)
            driver.find_element_by_css_selector("body > div.main > a").click()
            logging.info('detection DHCP success')
            time.sleep(5)
            try:
                driver.find_element_by_id("key").is_displayed()
                return 1
            except:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/detection_DHCP-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('detection fail %s' % e)
            return 0
        finally:
            pass


    ####WAN口未连接网线####
    def initialize_skip(self, driver):
        time.sleep(15)
        try:
            #driver.find_element_by_link_text(u"跳过检测").click()
            time.sleep(3)
            driver.find_element_by_id("key").clear()
            time.sleep(3)
            driver.find_element_by_id("key").send_keys("12345678")
            time.sleep(3)
            driver.find_element_by_id("wifi").click()
            time.sleep(10)
            #driver.find_element_by_link_text(u"登录路由器").click()
            time.sleep(10)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/initialize_skip-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize skip fail %s" % e)
            return 0
        finally:
            pass


    ####WAN口连接PPPOE网线####
    def detection_pppoe(self, driver, pppoe_user, pppoe_pw):
        try:
            #driver.find_element_by_class_name("btn").click()
            #time.sleep(3)
            logging.info("pppoe configuration")
            driver.find_element_by_id("username").clear()
            time.sleep(1)
            driver.find_element_by_id("username").send_keys(pppoe_user)
            time.sleep(1)
            driver.find_element_by_id("password").clear()
            time.sleep(1)
            driver.find_element_by_id("password").send_keys(pppoe_pw)
            time.sleep(3)
            driver.find_element_by_id("pppoe").click()
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/detection-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("initialize pppoe fail  %s" % e)
            return 0
        finally:
            pass


    ####初始化配置wifi密码####
    def initialize_pw(self, driver, default_pw):
        time.sleep(5)
        try:
            driver.find_element_by_id("key")
            driver.find_element_by_id("key").clear()
            time.sleep(1)
            driver.find_element_by_id("key").send_keys(default_pw)
            time.sleep(3)
            logging.info("save initialize password == %s" % default_pw)
            driver.find_element_by_id("wifi").click()
            logging.info("set initialize password success")
            time.sleep(10)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/initialize_pw-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("initialize set wifi fail %s" % e)
            return 0
        finally:
            pass


    ####设置wifi SSID####
    def setssid(self, driver):
        time.sleep(2)
        try:
            driver.find_element_by_id("ssid")
            driver.find_element_by_id("ssid").clear()
            time.sleep(1)
            driver.find_element_by_id("ssid").send_keys("dt_test")
            logging.info("initialize set wifi ssid success")
            time.sleep(3)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(
                os.path.dirname(os.getcwd()) + "/errorpng/setssid-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize set wifi SSID fail %s" % e)
            return 0
        finally:
            pass


    ####获取wifi SSID####
    def getssid(self, driver):
        try:
            #driver.find_element_by_id("ssid")
            texts=driver.find_element_by_id("ssid").get_attribute("value")
            logging.info(texts)
            time.sleep(1)
            logging.info("initialize get wifi ssid success")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getssid-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize get wifi ssid fail %s" % e)
            return 0
        finally:
            pass


    ###完成初始化配置###
    def complete(self, driver):
        time.sleep(2)
        try:
            #driver.find_element_by_css_selector("body > div.main > a").click()
            #time.sleep(5)
            logging.info("complete success-setupWizard")
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/complete-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("initialize complete fail %s" % e)
            return 0
        finally:
            pass


    ###获取初始化首页文本###
    def texthome(self, driver):
        try:
            texthomes=driver.find_element_by_class_name("init-text").text
            logging.info(texthomes)
            if texthomes == "欢迎体验newifi 路由器，请简单设置完成初始化配置":
                logging.info("welcome case success!")
            else:
                logging.warning("get welcome fail")
            ######
            texthomes2=driver.find_element_by_class_name("init-protocol-text").text
            logging.info(texthomes2)
            if texthomes2 == "我已阅读并同意《newifi 路由器用户协议》和《搜狐共享服务协议》，并同意开启搜狐视频加速服务。":
                logging.info("agreement case success!")
            else:
                logging.warning("get agreement fail")
            ###左边栏###
            lefttext=driver.find_element_by_class_name("aside-content").text
            logging.info(lefttext)
            if lefttext == "初始化":
                logging.info("left case success!")
            else:
                logging.warning("get left fail")
            return 1
        except Exception as e:
            logging.warning("get initialize home fail %s" % e)
            return 0
        finally:
            pass


    ###获取WIFI设置页面文本内容###
    def textwifi(self, driver):
        ###获取-wifi设置###
        lefttext=driver.find_element_by_class_name("aside-content").text
        print(lefttext)
        ###获取-请输入WiFi名称和密码###
        textsp=driver.find_element_by_css_selector("body > div.main > table > thead > tr > th:nth-child(2)").text
        print(textsp)
        ###获取-初始化设置WiFi密码将作为路由器登录密码###
        textpp=driver.find_element_by_class_name("form-text").text
        print(textpp)