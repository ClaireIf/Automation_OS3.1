import time,logging
from appium import webdriver

class set_APP:
    def set_app(self,driver):
        time.sleep(3)
        logging.info(u"====点击“设置”====")
        driver.find_element_by_id("com.diting.newifi.bridge:id/radBtn_Setting").click()
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/wifiSettingBtn").is_displayed()
            logging.info("======成功进入设置页面======")
            return 1
        except:
            logging.error("=========进入设置页面出错==========")
            return 0

    def click_wifi(self,driver):
        time.sleep(2)
        logging.info("点击进入WiFi设置")
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/wifiSettingBtn").click()
            time.sleep(1)
            return 1
        except Exception as e:
            return 0

    def click_24Gwifi_switch(self, driver, switchChoose):
        time.sleep(2)
        logging.info('========点击 2.4G wifi开关=========')
        try:
            driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_switch")[0].click()
            time.sleep(3)
            if switchChoose == 1:
                logging.info("====== 确定 =====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if switchChoose == 2:
                logging.info("===== 取消 ====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except Exception as e:
            return 0

    def set_24Gwifi_SSID_PW(self, driver, SSID, wifi_PW,wifiChoose):
        time.sleep(2)
        logging.info('======2.4G 修改名称/密码 =====')
        driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_alter_layout")[0].click()
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/wifi_alter_name").send_keys(SSID)
            time.sleep(1)
            driver.find_element_by_id("com.diting.newifi.bridge:id/wifi_alter_pwd").send_keys(wifi_PW)
            time.sleep(1)
            if wifiChoose ==1:
                logging.info("===确定====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/rightTv").click()
                return 1
            if wifiChoose ==2:
                logging.info('====取消====')
                driver.find_element_by_id("com.diting.newifi.bridge:id/goBackBtn").click()
                return 2
        except Exception as e:
            return 0


    def set_24Gwifi_encryption(self,driver,encrChoose,encrChoose2):
        time.sleep(2)
        logging.info('=======2.4G 加密方式=======')
        driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_encrypt_layout")[0].click()
        try:
            if encrChoose ==1:
                driver.find_element_by_android_uiautomator('new UiSelector().text("（WPA2）")').click()
            if encrChoose ==2:
                driver.find_element_by_android_uiautomator('new UiSelector().text("（WPA/WPA2）")').click()
            if encrChoose ==3:
                driver.find_element_by_android_uiautomator('new UiSelector().text("（允许所有人连接）').click()
            if encrChoose2 ==1:
                logging.info("===确定====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/rightTv").click()
                return 1
            if encrChoose2 ==2:
                logging.info('====取消====')
                driver.find_element_by_id("com.diting.newifi.bridge:id/goBackBtn").click()
                return 2
        except Exception as e:
            return 0


    def set_24Gwifi_hide(self,driver, hideChoose):
        time.sleep(2)
        logging.info("=======2.4G 隐藏网络========")
        try:
            driver.find_element_by_id("com.diting.newifi.bridge:id/wifi_setting_hide_switch")[0].click()
            time.sleep(3)
            if hideChoose == 1:
                logging.info("====== 确定 =====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if hideChoose == 2:
                logging.info("===== 取消 ====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except Exception as e:
            return 0


    def click_5Gwifi_switch(self, driver,switchChoose_5G):
        time.sleep(2)
        logging.info('========点击 5G wifi开关=========')
        try:
            f = driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_switch")[1]
            f.click()
            time.sleep(3)
            if switchChoose_5G == 1:
                logging.info("====== 确定 =====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if switchChoose_5G == 2:
                logging.info("===== 取消 ====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except Exception as e:
            logging.error("点击 5G wifi 开关出错 %s" % e)
            return 0

    def set_5Gwifi_SSID_PW(self,driver,SSID_5G,wifi_PW_5G,wifiChoose2):
        time.sleep(2)
        logging.info('====== 5G 修改名称/密码 =====')
        driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_alter_layout")[1].click()
        time.sleep(5)
        try:
            ssid = driver.find_element_by_id("com.diting.newifi.bridge:id/wifi_alter_name")
            ssid.clear()
            ssid.send_keys(SSID_5G)
            time.sleep(1)
            ssidpw = driver.find_element_by_id("com.diting.newifi.bridge:id/wifi_alter_pwd")
            ssidpw.clear()
            ssidpw.send_keys(wifi_PW_5G)
            time.sleep(1)
            if wifiChoose2 ==1:
                logging.info("===确定====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/rightTv").click()
                return 1
            if wifiChoose2 ==2:
                logging.info('====取消====')
                driver.find_element_by_id("com.diting.newifi.bridge:id/goBackBtn").click()
                return 2
        except Exception as e:
            return 0

    def set_5Gwifi_encryption(self,driver, encrChoose_5G, encrChoose_5G2):
        time.sleep(2)
        logging.info('=======5G 加密方式=======')
        driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_encrypt_layout")[1].click()
        # f = driver.find_element_by_class_name("android.widget.TextView")[1]
        # f.click()
        try:
            if encrChoose_5G ==1:
                driver.find_element_by_android_uiautomator('new UiSelector().text("（WPA2）")').click()
            if encrChoose_5G ==2:
                driver.find_element_by_android_uiautomator('new UiSelector().text("（WPA/WPA2）")').click()
            if encrChoose_5G ==3:
                driver.find_element_by_android_uiautomator('new UiSelector().text("（允许所有人连接）').click()
            if encrChoose_5G2 ==1:
                logging.info("===确定====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/rightTv").click()
                return 1
            if encrChoose_5G2 ==2:
                logging.info('====取消====')
                driver.find_element_by_id("com.diting.newifi.bridge:id/goBackBtn").click()
                return 2
        except Exception as e:
            return 0

    def set_5Gwifi_hide(self, driver, hideChoose_5G):
        time.sleep(2)
        logging.info("=======5G 隐藏网络========")
        try:
            driver.find_elements_by_id("com.diting.newifi.bridge:id/wifi_setting_hide_switch")[1].click()
            time.sleep(5)
            if hideChoose_5G == 1:
                logging.info("====== 确定 =====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if hideChoose_5G == 2:
                logging.info("===== 取消 ====")
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except Exception as e:
            return 0


    def restart_app(self,driver,restartChoose):
        time.sleep(2)
        logging.info("====点击“重启”=========")
        driver.find_element_by_id("com.diting.newifi.bridge:id/btnRestartRouter").click()
        try:
            time.sleep(2)
            if restartChoose ==1:
                logging.info("确定重启")
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if restartChoose ==2:
                logging.info("取消重启")
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except:
            logging.error("=======重启出错==========")
            return 0

    def reset_app(self,driver,resetChoose):
        time.sleep(2)
        logging.info("======点击“重置”=======")
        driver.find_element_by_id("com.diting.newifi.bridge:id/btnResetRouter").click()
        try:
            time.sleep(7)
            if resetChoose ==1:
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                return 1
            if resetChoose ==2:
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except:
            logging.error("======重置出错==========")
            return 0

    def upgradeRouter_app(self,driver,upgradeChoose):
        time.sleep(3)
        driver.swipe(300, 900, 300, 500)
        time.sleep(3)
        logging.info("======点击“升级”=======")
        driver.find_element_by_id("com.diting.newifi.bridge:id/layoutRouterVerCheck").click()
        try:
            time.sleep(5)
            if upgradeChoose ==1:
                logging.info("=====升级=======")
                driver.find_element_by_id("com.diting.newifi.bridge:id/upgradeBtn").click()
                return 1
            if upgradeChoose ==2:
                logging.info("======取消升级=======")
                driver.find_element_by_id("com.diting.newifi.bridge:id/imgClose").click()
                return 2
        except:
            logging.error("======升级出错==========")
            return 0


    def changeAdminPW(self, driver):
        time.sleep(3)
        try:
            logging.info('===点击修改管理员密码===')
            driver.find_element_by_id("com.diting.newifi.bridge:id/alterAdminPassword").click()
            time.sleep(3)
            try:
                driver.find_element_by_id("com.diting.newifi.bridge:id/password_set_pwd").is_displayed()
                return 1
            except:
                logging.error('进入修改管理员密码页面出错')
                return 2
        except Exception as e:
            logging.error("%s" % e)
            return 0

    def set_AdminPW(self, driver,onePW,surePW,choosePW):
        time.sleep(2)
        try:
            logging.info('=====输入新管理员密码====')
            driver.find_element_by_id("com.diting.newifi.bridge:id/password_set_pwd").send_keys(onePW)
            driver.find_element_by_id("com.diting.newifi.bridge:id/password_set_repwd").send_keys(surePW)
            if choosePW ==1:
                logging.info('确定修改管理员密码')
                driver.find_element_by_id("com.diting.newifi.bridge:id/rightTv").click()
                return 1
            if choosePW ==2:
                logging.info('取消修改管理员密码')
                driver.find_element_by_id("com.diting.newifi.bridge:id/goBackBtn").click()
                return 2
        except Exception as e:
            logging.error("%s" % e)
            return 0

    def tools_click(self, driver):
        try:
            logging.info('点击“实用工具”')
            driver.find_element_by_id('com.diting.newifi.bridge:id/btnTools').click()
            time.sleep(5)
            return 1
        except:
            logging.error('点击实用工具出错')
            return 0


    def tools_installed(self,driver):
        time.sleep(3)
        try:
            logging.info('进入已安装')
            # driver.find_element_by_id('com.diting.newifi.bridge:id/imgHead').is_displayed()
            # driver.find_element_by_link_text("已安装").click()
            driver.find_element_by_android_uiautomator('new UiSelector().text("已安装")').click()
            logging.info('已安装samba')
            time.sleep(5)
            return 1
        except:
            logging.error('进入已安装出错')
            return 0

    def tools_online(self, driver):
        time.sleep(5)
        try:
            logging.info("进入待安装")
            # driver.find_element_by_id('com.diting.newifi.bridge:id/tabItemTitle').click()
            # driver.find_element_by_partial_tag_name("待安装").click()
            driver.find_element_by_android_uiautomator('new UiSelector().text("待安装")').click()
            return 1
        except Exception as e:
            logging.error('进入待安装出错=====%s' % e)
            return 0

    def tools_install(self, driver):
        try:
            logging.info("安装插件")
            driver.find_element_by_id("com.diting.newifi.bridge:id/btnOk").click()
            time.sleep(50)
            return 1
        except Exception as e:
            logging.info("安装插件出错====%s" % e)
            return 0

    def tools_getInstalled(self, driver):
        time.sleep(5)
        try:
            logging.info('获取已安装插件')
            driver.find_element_by_android_uiautomator('new UiSelector().text("迅雷远程下载")').is_displayed()
            logging.info("已安装迅雷远程下载")
            return 1
        except Exception as e:
            logging.error("====未发现迅雷远程下载插件=====%s" % e)
            return 0
        finally:
            pass

    def tools_uninstall(self, driver, unChoose):
        time.sleep(3)
        try:
            logging.info("=====卸载插件=====")
            driver.find_element_by_id("com.diting.newifi.bridge:id/btnOk").click()
            time.sleep(2)
            if unChoose ==1:
                logging.info("确定卸载")
                driver.find_element_by_id("com.diting.newifi.bridge:id/positiveButton").click()
                time.sleep(10)
                return 1
            if unChoose ==2:
                logging.info("取消卸载")
                driver.find_element_by_id("com.diting.newifi.bridge:id/negativeButton").click()
                return 2
        except Exception as e:
            logging.error("====卸载插件出错=====%s" % e)
            return 0