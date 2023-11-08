from selenium import webdriver
import pytest
import configparser
import os
driver = None
projectpath = os.path.dirname(os.getcwd())
config_file = projectpath + '/configure/' + 'testconfig.ini'
# result_dir = projectpath + '/errorpng/'

config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
model = config.get('Default', 'model')

if model == 'newifi 新路由 Y1S':
    img_url = 'http://192.168.102.200:8080/job/Y1S%20full%20case/ws'
if model == 'newifi 新路由 mini':
    img_url = 'http://192.168.102.200:8080/job/Y1%20full%20case/ws'
if model == 'newifi 新路由 2':
    img_url = 'http://192.168.102.200:8080/job/D1%20full%20case/ws'
if model == 'newifi 新路由 3':
    img_url = 'http://192.168.102.200:8080/job/D2%20full%20case/ws'

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            imageFile = os.path.dirname(os.getcwd())+'/errorpng/caseFail/'+file_name
            imageURLFile = '/errorpng/caseFail/'+file_name
            _capture_screenshot(imageFile)
            if file_name:
                html = '<div><img src="%s%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' %(img_url,imageURLFile)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    # driver.get_screenshot_as_file(name)
    pass

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.close()
        driver.quit()
    else:
        driver = webdriver.Chrome()
    print('one %s'%driver)
    return driver

