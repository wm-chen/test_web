# encoding: utf-8
# author: wm-chen
# assert_utils.py
# 2021/7/28 3:55 下午
# desc:
from selenium.webdriver.support.wait import WebDriverWait
from CLover_Ui_Test.clover_app.common.log_utils import logger


class AssertUtils:

    def __init__(self, _driver):
        self.driver = _driver

    # 定位元素的方法
    def find_element(self, element_info):
        locator_type = element_info['断言定位类型']
        locator_value = element_info['定位值']
        wait_time = int(element_info['等待时间']) if element_info['等待时间'] or element_info['等待时间'] == '0' else 10
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
        except Exception as e:
            logger.error('断言元素识别失败, 失败原因 %s' % e)
        return element

    # 定位元素的方法
    def find_elements(self, element_info):
        locator_type = element_info['断言定位类型']
        locator_value = element_info['定位值']
        locator_index = int(element_info['定位下标'])
        wait_time = int(element_info['等待时间']) if element_info['等待时间'] or element_info['等待时间'] == '0' else 10
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
        except Exception as e:
            logger.error('断言元素识别失败, 失败原因 %s' % e)
        return element[locator_index]

    def assert_utils(self, element_info):
        if element_info['定位下标'] == '':
            element = self.find_element(element_info)
        else:
            element = self.find_elements(element_info)
        if element_info['取值类型'] in ['contentDescription', 'resourceId', 'className']:
            return element.get_attribute(element_info['取值类型'])
        elif element_info['取值类型'] == 'text':
            return element.text
