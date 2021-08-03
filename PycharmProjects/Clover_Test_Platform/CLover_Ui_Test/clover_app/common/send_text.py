# encoding: utf-8
# author: wm-chen
# send_text.py
# 2021/7/26 2:58 下午
# desc:
import time
from selenium.webdriver.support.wait import WebDriverWait


class SendText:

    def __init__(self, driver):
        self.key_table = {
            '0': 7, '1': 8, '2': 9, '3': 10,  '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
            'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38,
            'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48,
            'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
            'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
            'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
            'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
            ' ': 62, '\\': 73, '，': 55, '`': 68, '[': 71, '—': 69, '+': 157, ',': 159, '/': 154,
            '.': 158, '=': 161, '(': 162, '*': 155, ')': 163, '-': 156, ']': 72, ';': 74
        }
        self.driver = driver

    def send_text(self, text):
        text_list = list(','.join(text).split(','))
        time.sleep(1)
        for i in text_list:
            if 65 <= ord(i) <= 90:
                WebDriverWait(self.driver, 10).until(lambda x: x.press_keycode(self.key_table[i], 1))
            else:
                WebDriverWait(self.driver, 10).until(lambda x: x.press_keycode(self.key_table[i]))
