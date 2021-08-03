# encoding: utf-8
# author: wm-chen
# test_utils.py
# 2021/8/2 4:54 下午
# desc:
import allure
import pytest
from CLover_Ui_Test.clover_app.run_all_cases import run_all_case
from CLover_Ui_Test.clover_app.common.case_utils import CaseUtils
from CLover_Ui_Test.clover_app.common.assert_utils import AssertUtils


cases = []


def get_case(modeladmin, request, queryset):
    global cases
    for obj in queryset:
        case = {
            '用例版本': obj.project_case.project_name + obj.project_case.project_version,
            '用例名称': obj.case_name,
            '用例说明': obj.case_description,
            '是否执行': obj.run,
            '期望结果': obj.export if '\\n' not in obj.export else obj.export.replace('\\n', '\n'),
            '断言数据': {
                '断言定位类型': obj.assert_type,
                '定位值': obj.assert_value,
                '取值类型': obj.text_type,
                '定位下标': obj.assert_subscript,
                '等待时间': obj.assert_time,
            },
            '用例参数': obj.param_data,
            '所属模块': obj.case_scene.model_name,
            '用例动作': obj.case_scene.scene_actions.all()
        }
        cases.append(case)
    if run_all_case() == 0:
        cases.clear()


@allure.epic('Clover App Ui自动化测试')
class TestUtils:

    @pytest.mark.parametrize('re_start', cases, indirect=True)
    def test_utils(self, re_start):
        driver, case_data = re_start
        CaseUtils(driver, case_data['用例动作'], case_data['用例参数']).case_utils()
        result = AssertUtils(driver).assert_utils(case_data['断言数据'])
        assert case_data['期望结果'] in result

