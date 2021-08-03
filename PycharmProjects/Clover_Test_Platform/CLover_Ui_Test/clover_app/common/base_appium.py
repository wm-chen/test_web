# encoding: utf-8
# author: wm-chen
# base_appium.py
# 2021/4/28 4:24 下午
# desc:
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from CLover_Ui_Test.clover_app.common.log_utils import logger
from CLover_Ui_Test.clover_app.common.send_text import SendText
import allure


class BaseAppium(object):

    def __init__(self, _driver):
        self.driver = _driver

    # 定位元素的方法
    def find_element(self, element_info):
        locator_type = element_info['定位类型']
        locator_value = element_info['定位值']
        wait_time = element_info['等待时间']
        # ID定位（取 resource_id 、id 、 name）
        try:
            if locator_type == 'id':
                element = WebDriverWait(self.driver, wait_time). \
                    until(lambda x: x.find_element_by_id(locator_value))
            # class定位 （取 class）
            elif locator_type == 'class':
                element = WebDriverWait(self.driver, wait_time). \
                    until(lambda x: x.find_element_by_class_name(locator_value))
            elif locator_type == 'xpath':
                element = WebDriverWait(self.driver, wait_time). \
                    until(lambda x: x.find_element_by_xpath(locator_value))
            # AccessibilityId定位 （取content-desc）
            elif locator_type == 'content':
                element = WebDriverWait(self.driver, wait_time).\
                    until(lambda x: x.find_element_by_accessibility_id(locator_value))
            # Android定位
            elif locator_type == 'android':
                element = WebDriverWait(self.driver, wait_time).\
                    until(lambda x: x.find_element_by_android_uiautomator(locator_value))
            return element
        except Exception:
            return False

    def find_elements(self, element_info):
        locator_type = element_info['定位类型']
        locator_value = element_info['定位值']
        wait_time = element_info['等待时间']
        locator_index = element_info['定位下标']
        # ID定位（取 resource_id 、id 、 name）
        try:
            if locator_type == 'id':
                element = WebDriverWait(self.driver, wait_time). \
                    until(lambda x: x.find_elements_by_id(locator_value))
            # class定位 （取 class）
            elif locator_type == 'class':
                element = WebDriverWait(self.driver, wait_time). \
                    until(lambda x: x.find_elements_by_class_name(locator_value))
            elif locator_type == 'xpath':
                element = WebDriverWait(self.driver, wait_time). \
                    until(lambda x: x.find_elements_by_xpath(locator_value))
            # AccessibilityId定位 （取content-desc）
            elif locator_type == 'content':
                element = WebDriverWait(self.driver, wait_time).\
                    until(lambda x: x.find_elements_by_accessibility_id(locator_value))
            # Android定位
            elif locator_type == 'android':
                element = WebDriverWait(self.driver, wait_time).\
                    until(lambda x: x.find_elements_by_android_uiautomator(locator_value))
            return element[int(locator_index)]
        except Exception:
            return False

    # 发送文本前先清空
    def send(self, element, value, description):
        try:
            element.click()
            SendText(self.driver).send_text(value)
            with allure.step('向【%s】输入：%s' % (description, value)):
                logger.info('元素%s send成功' % description)
        except Exception as e:
            with allure.step('向【%s】输入：%s 失败' % (description, value)):
                logger.error('元素%s send失败,失败原因%s' % (description, e))

    def click(self, element, description):
        try:
            element.click()
            with allure.step('点击【%s】' % description):
                logger.info('元素%s click成功' % description)
        except Exception as e:
            with allure.step('点击【%s】' % description):
                logger.error('元素%s click失败，失败原因 %s' % (description, e))

    # 安装app
    def install(self, app_path):
        self.driver.install_app(app_path=app_path)

    # 卸载app
    def remove(self, app_name):
        self.driver.remove_app(app_name)

    # 判断APP是否安装，传递的参数为包名
    def is_install(self, app_name):
        self.driver.is_app_installed(app_name)

    # 关闭app
    def close(self):
        self.driver.close()

    # 重启app,清除数据
    def restart(self):
        self.driver.reset()

    # 重启app，不清楚数据
    def launch(self):
        self.driver.launch_app()

    # app后台运行
    def background(self, times):
        self.driver.background_app(times)

    # 获取元素属性值
    def attribute_text(self, element, value):
        # 获取content-desc contentDescription,获取元素的resource-id属性值 resourceId,获取元素的class属性值 className
        text = element.get_attribute(value)
        return text

    # 获取剪切板内容
    def clipboard_text(self):
        return self.driver.get_clipboard_text()

    # 根据页面获取的context-desc,获取元素
    def context_desc(self, value):
        element = WebDriverWait(self.driver, 100).until(lambda x: x.find_element_by_accessibility_id(value))
        return element

    # 屏幕滑动
    def swipe_sign(self, direction):
        size = driver.get_window_size()
        if direction == '上':
            driver.swipe(size['width'] / 2, size['height'] / 2, size['width'] / 2, 0)
        elif direction == '下':
            driver.swipe(size['width'] / 2, size['height'] / 2, size['width'] / 2, size['height'] - 10)
        elif direction == '左':
            driver.swipe(size['width'] / 2, size['height'] / 2, 0, size['height'] / 2)
        elif direction == '右':
            driver.swipe(size['width'] / 2, size['height'] / 2, size['width'] - 10, size['height'] /2)
        else:
            logger.error('滑动操作只能输入上下左右')


if __name__ == '__main__':
    driver = webdriver.Remote()
