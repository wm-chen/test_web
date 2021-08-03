from django.db import models
import re


def get_action():

    with open('/Users/weimaochen/PycharmProjects/Clover_Test_Platform/CLover_Ui_Test/clover_app/common/base_appium.py', 'r') as file:
        text = file.read()
    result = re.findall("def (.+?)\(", text)
    aa = ((x, x) for x in result[1:])
    return tuple(aa)


class PageAction(models.Model):
    page_name = models.CharField(
        '页面名称',
        max_length=20,
        choices=(
            ('send_page', '交易页面'),
            ('assert_page', '资产页面'),
            ('swap_page', 'swap页面'),
            ('set_page', '设置页面'),
            ('cross_page', '跨链交易页面'),
            ('detail_page', '资产详情页面')
        )
    )
    element_name = models.CharField('元素名称', max_length=20)
    element_description = models.CharField('元素详情', max_length=20, blank=True)
    locate_type = models.CharField(
        '定位方法',
        max_length=20,
        choices=(
            ('id', 'id'),
            ('class', 'class'),
            ('xpath', 'xpath'),
            ('content', 'content-desc'),
            ('android', 'android'),
        )
    )
    locate_action = models.CharField(
        '操作动作',
        max_length=20,
        choices=get_action(),
    )
    locate_value = models.CharField('定位值', max_length=100)
    locate_subscript = models.CharField('定位下标', max_length=10, blank=True)
    locate_time = models.CharField('等待时间', max_length=5)
    key_name = models.CharField('参数的key_name', max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '页面动作管理'
        verbose_name = '页面动作管理'

    def __str__(self):
        return self.page_name + '.' + self.element_name


class PageScene(models.Model):
    model_name = models.CharField(
        '所属模块',
        max_length=20,
        choices=(
            ('send_model', '交易模块'),
            ('assert_model', '资产模块'),
            ('swap_model', 'swap模块'),
            ('set_model', '设置模块'),
            ('cross_model', '跨链交易模块'),
            ('detail_model', '资产详情模块')
        ),
    )
    scene_name = models.CharField('场景名称', max_length=20)
    scene_description = models.CharField('场景介绍', max_length=50)
    scene_actions = models.ManyToManyField(
        PageAction,
        through='SceneAction',
        through_fields=('scene_name', 'action_list'),
        verbose_name='场景动作列表'
    )
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '场景管理'
        verbose_name = '场景管理'

    def __str__(self):
        return '%s(%s)' % (self.scene_name, self.scene_description)


class SceneAction(models.Model):
    action_list = models.ForeignKey(PageAction, on_delete=models.CASCADE)
    scene_name = models.ForeignKey(PageScene, on_delete=models.CASCADE)
    key_name = models.CharField('参数的key_name', max_length=100, blank=True)


# 项目版本表
class ProjectVersion(models.Model):
    project_name = models.CharField(
        '项目名称',
        max_length=20,
        choices=(
            ('app_ui_test', 'app自动化'),
            ('web_ui_test', 'web自动化'),
            ('api_test', '接口自动化'),
        ),
        default=True,
    )
    project_version = models.CharField('版本号', max_length=50)

    class Meta:
        # 排序
        ordering = ["project_name"]
        # 显示的复数名
        verbose_name_plural = '项目管理'
        verbose_name = '项目管理'
        # 联合约束
        unique_together = [['project_name', 'project_version'], ]

    def __str__(self):
        return self.project_name + ' ' + self.project_version


# 项目case表
class AppUiCase(models.Model):
    project_case = models.ForeignKey(
        ProjectVersion,
        on_delete=models.CASCADE,
        limit_choices_to={'project_name': 'app_ui_test'},
        verbose_name='项目版本',
    )
    case_scene = models.ForeignKey(
        PageScene,
        on_delete=models.CASCADE,
        verbose_name='用例场景',
    )
    case_name = models.CharField('用例名称', max_length=50)
    case_description = models.CharField('用例说明', max_length=100)
    run = models.BooleanField(default=True)
    export = models.CharField('期望结果', max_length=50, blank=True)
    assert_type = models.CharField(
        '断言定位类型',
        choices=(
            ('id', 'id'),
            ('class', 'class'),
            ('xpath', 'xpath'),
            ('content', 'content-desc'),
            ('android', 'android'),
        ),
        max_length=50,
        blank=True)
    assert_value = models.CharField('断言定位值', max_length=50, blank=True)
    text_type = models.CharField('取值类型', max_length=50, blank=True)
    assert_subscript = models.CharField('定位下标', max_length=50, blank=True)
    assert_time = models.CharField('断言元素等待时间', max_length=50, blank=True)
    param_data = models.JSONField('用例参数', blank=True)

    class Meta:
        verbose_name_plural = 'app用例管理'
        verbose_name = 'app用例管理'

    def __str__(self):
        return self.case_name


# case记录表
class CaseRecord(models.Model):
    case_list = models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)

