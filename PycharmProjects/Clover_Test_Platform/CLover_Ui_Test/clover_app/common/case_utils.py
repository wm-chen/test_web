# encoding: utf-8
# author: wm-chen
# case_utils.py
# 2021/8/3 11:20 上午
# desc:
from CLover_Ui_Test.clover_app.common.base_appium import BaseAppium


class CaseUtils(BaseAppium):

    def __init__(self, driver, case_actions, case_param):
        super().__init__(driver)
        self.case_actions = case_actions
        self.case_param = case_param

    def case_utils(self):
        for case_action in self.case_actions:
            element_info = {
                '定位类型': case_action.locate_type,
                '定位值': case_action.locate_value,
                '等待时间': int(case_action.locate_time),
                '定位下标': case_action.locate_subscript
            }
            if case_action.locate_subscript or case_action.locate_subscript == 0:
                element = self.find_elements(element_info)
            else:
                element = self.find_element(element_info)
            if case_action.locate_action == 'send':
                self.send(element, self.case_param[case_action.key_name], case_action.element_description)
            elif case_action.locate_action == 'click':
                self.click(element, case_action.element_description)
            elif case_action.locate_action == 'clipboard_text':
                self.clipboard_text()
            elif case_action.locate_action == 'swipe_sign':
                self.swipe_sign(self.case_param[case_action.key_name])
            elif case_action.locate_action == 'find_element' or case_action.locate_action == 'find_elements':
                if element:
                    continue
                else:
                    break


if __name__ == '__main__':
    pass
