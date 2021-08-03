# encoding: utf-8
# author: wm-chen
# config_util.py
# 2021/4/28 3:55 下午
# desc:获取配置文件
import configparser
import os


class ConfigUtil:

    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__),'../config/config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(self.config_path, encoding='utf-8')

    @property
    def get_platformName(self):
        value = self.cf.get('device', 'platformName')
        return value

    @property
    def get_platformVersion(self):
        value = self.cf.get('device', 'platformVersion')
        return value

    @property
    def get_deviceName(self):
        value = self.cf.get('device', 'deviceName')
        return value

    @property
    def get_udid(self):
        value = self.cf.get('device', 'udid')
        return value

    @property
    def get_appPackage(self):
        value = self.cf.get('app', 'appPackage')
        return value

    @property
    def get_appActivity(self):
        value = self.cf.get('app', 'appActivity')
        return value

    @property
    def get_url(self):
        value = self.cf.get('appium', 'url')
        return value


config = ConfigUtil()
if __name__ == '__main__':
    config = ConfigUtil()
    print(config.get_udid)
