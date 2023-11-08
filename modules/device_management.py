# -*- coding:utf-8 -*-
###################################
#   设备管理
###################################
import os
import time
import logging

class device_management:
    ##########
    #访问设置
    ##########
    def devicesManagement(self, driver,clickChoose):
        time.sleep(2)
        try:
            logging.info('=== click Access Setting ===')
            driver.find_element_by_link_text(u"设备管理").click()
            time.sleep(5)
            if clickChoose == 1:
                logging.info('Access Setting ')
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(1) > a").click()
                return 1
            if clickChoose == 2:
                logging.info("Auto Speed Limit")
                driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(2) > a").click()
                time.sleep(3)
                getSpeed = driver.find_element_by_css_selector("#map > div.limit-off > p").text
                logging.info("getSpeed ===%s" %getSpeed)
                if getSpeed == '智能限速未开启':
                    return 2
                else:
                    return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/devicesManagement-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error('====devicesManagement error==== %s' %e)
            return 0
        finally:
            pass


    def getStatus(self,driver):
        try:
            logging.info('GET Status')
            status = driver.find_element_by_xpath("//*[@id='sectionitem_deviceAccSection']/div/div[3]/div").get_attribute('unable')
            logging.info('============= %s' % status)
        except:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getStatus-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            return 0
        finally:
            pass

    ##########
    #访问外网
    ##########
    def AccessNetwork(self, driver):
        time.sleep(2)
        try:
            logging.info('click Access Network')
            driver.find_element_by_xpath("//*[@id='sectionitem_deviceAccSection']/div/div[3]/div").click()
            time.sleep(2)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/AccessNetwork-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error('====Access Setting erro==== %s' %e)
            return 0
        finally:
            pass


    ##############
    #访问Samba
    ##############
    def AccessSamba(self, driver,sambaChoose):
        time.sleep(2)
        try:
            logging.info('=== Click Access Samba ===')
            driver.find_element_by_css_selector("#sectionitem_deviceAccSection > div > div.acc-column-four > div").click()
            time.sleep(10)
            # getSamba = driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > p").text
            # if getSamba=="关闭全盘访问权限后，该设备将无法访问内网资源，确定关闭？":
            if sambaChoose == 1:
                logging.info("=== Sure ===")
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
                time.sleep(5)
                return 1
            if sambaChoose == 2:
                logging.info("=== Cancel ===")
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel").click()
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/AccessSamba-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error('====Access Samba error==== %s' % e)
            return 0
        finally:
            pass


    #############
    # 修改设备名
    #############
    def changeDeviceName(self, driver, test_device):
        logging.info("changeDeviceName is Running")
        time.sleep(2)
        try:
            logging.info('click Access Setting')
            driver.find_element_by_link_text(u"设备管理").click()
            time.sleep(2)
            logging.info('click Edit Device')
            # 点击修改设备名
            driver.find_element_by_xpath("//*[@id=\"sectionitem_deviceAccSection\"]/div/div[1]/div/div/img").click()
            time.sleep(2)
            driver.find_element_by_css_selector("input.acc-input-name").clear()
            time.sleep(2)
            driver.find_element_by_css_selector("input.acc-input-name").send_keys(test_device)
            time.sleep(2)
            # 刷新
            driver.find_element_by_xpath("//*[@id=\"acc_refresh\"]").click()
            time.sleep(2)
            # driver.find_element_by_link_text(u"路由设置").click()
            # time.sleep(2)
            # driver.find_element_by_link_text(u"系统设置").click()
            # time.sleep(2)
            # driver.find_element_by_id("btn_re_boot").click()
            # time.sleep(4)
            # driver.find_element_by_css_selector(
            #     "body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            # time.sleep(90)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/changeDeviceName-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            return 0
        finally:
            pass


    def checkDeviceName(self, driver,test_device):
        print("checkDeviceName is Running")
        time.sleep(2)
        logging.info('click Access Setting')
        driver.find_element_by_link_text(u"设备管理").click()
        time.sleep(2)
        temp = driver.find_element_by_xpath("//*[@id=\"sectionitem_deviceAccSection\"]/div/div[1]/div/div/span[1]").text
        if temp == test_device:
            return 1
        else:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/checkDeviceName-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            return 0


    ###智能测速###
    def testSpeed(self,driver):
        time.sleep(2)
        try:
            logging.info("Click Test Speed")
            driver.find_element_by_css_selector("#map > div.limit-bar > a").click()
            time.sleep(120)
            getUp = driver.find_element_by_id("text_measure_up").text
            getDown = driver.find_element_by_id("text_measure_down").text
            logging.info("%s" %getUp)
            logging.info("%s" %getDown)
            if getUp !=None and getDown !=None:
                logging.info('TEST Speed Success')
                return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/testSpeed-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("=== Test Speed Error=== %s" % e)
            return 0
        finally:
            pass


    ###重新检测测速###
    def resurveySpeed(self,driver):
        time.sleep(2)
        try:
            logging.info("=== Resurvey Speed ===")
            driver.find_element_by_css_selector("#limit_measure_operate_check > button.newifi-btn.btn-green.limit-measure-operate-check").click()
            time.sleep(120)
            getUps = driver.find_element_by_id("text_measure_up").text
            getDowns = driver.find_element_by_id("text_measure_down").text
            logging.info("%s" %getUps)
            logging.info("%s" %getDowns)
            if getUps !=None and getDowns !=None :
                logging.info('TEST Speed Success')
                return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/resurveySpeed-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("=== Resurvey Speed Error === %s" % e)
            return 0
        finally:
            pass

    ###编辑限速上传、下载####
    def editSpeed(self, driver, up, down, editChoose):
        logging.info("=== Edit Speed ===")
        time.sleep(2)
        driver.find_element_by_id("limit_measure_edit").click()
        time.sleep(2)
        try:
            logging.info("Edit up")
            driver.find_element_by_id("input_measure_up").clear()
            driver.find_element_by_id("input_measure_up").send_keys(up)
            time.sleep(1)
            logging.info("Edit down")
            driver.find_element_by_id("input_measure_down").clear()
            driver.find_element_by_id("input_measure_down").send_keys(down)
            time.sleep(3)
            if editChoose ==1:
                logging.info("Click Sure")
                driver.find_element_by_id("limit_measure_save").click()
            if editChoose ==2:
                logging.info("Click Cancel")
                driver.find_element_by_id("limit_measure_cancel").click()
            time.sleep(3)
            getUp = driver.find_element_by_id("text_measure_up").text
            logging.info("Get UP ===%s" %getUp)
            getDown = driver.find_element_by_id("text_measure_down").text
            logging.info("Get Down ===%s" %getDown)
            if up == getUp and down == getDown:
                logging.info("===Edit Speed Save Success===")
                return 1
            else:
                logging.info("===Edit Speed Save Fail Or Cancel Save ====")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/resurveySpeed-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("=== Resurvey Speed Error=== %s" % e)
            return 0
        finally:
            pass


    def closeSpeed(self, driver):
        time.sleep(2)
        try:
            driver.find_element_by_css_selector("#map > div.limit-bar > a").click()
            time.sleep(3)
            getSpeed = driver.find_element_by_css_selector("#map > div.limit-off > p").text
            logging.info("getSpeed ===%s" %getSpeed)
            if getSpeed == '智能限速未开启':
                return 1
            else:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/closeSpeed-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error("=== Close Auto Speed Error=== %s" % e)
            return 0
        finally:
            pass