# encoding: utf-8
# author: wm-chen
# run_all_cases.py
# 2021/7/27 11:51 上午
# desc:
import os
import shutil
import pytest


def run_all_case():
    xml_path = os.path.join(os.path.dirname(__file__), 'report/xml_report/')
    html_report = os.path.join(os.path.dirname(__file__), 'report/html_report')
    if os.path.exists(xml_path):
        shutil.rmtree(xml_path)
    os.mkdir(xml_path)
    pytest.main(['CLover_Ui_Test/clover_app/testcases', '--alluredir=%s' % xml_path])
    text = os.system("allure generate %s/ -o %s --clean" % (xml_path, html_report))
    return text


if __name__ == '__main__':
    print(type(run_all_case()))

