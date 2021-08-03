# encoding: utf-8
# author: wm-chen
# conftest.py.py
# 2021/7/23 2:36 下午
# desc:
import time
import pytest
import allure
from appium import webdriver
from CLover_Ui_Test.clover_app.common.config_util import config
from CLover_Ui_Test.clover_app.common.send_text import SendText


@pytest.fixture(scope='session')
def start_app():
    des = {
        'platformName': config.get_platformName,  # 手机系统
        'platformVersion': config.get_platformVersion,  # 系统版本
        'deviceName': config.get_deviceName,  # 设备名称
        'udid': config.get_udid,  # 设备id
        # 'browserName':'chrome',                   # 启动谷歌浏览器
        'appPackage': config.get_appPackage,  # app包名
        'appActivity': config.get_appActivity,
        'noReset': True,  #
        'unicodeKeyboard': True,  # 中文
        'resetKeyboard': True,
        'automationName': 'UiAutomator2'
    }
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def re_start(request, start_app):
    case_data = request.param
    allure.dynamic.feature(case_data['用例版本'])
    allure.dynamic.story(case_data['所属模块'])
    allure.dynamic.title(case_data['用例名称'])
    allure.dynamic.description(case_data['用例说明'])
    driver = start_app
    driver.launch_app()
    time.sleep(5)
    driver.find_element_by_class_name('android.widget.EditText').click()
    SendText(driver).send_text('12345678')
    driver.find_element_by_accessibility_id('Unlock').click()
    return driver, case_data
