from django.contrib import admin
from .models import PageAction, PageScene, AppUiCase, ProjectVersion
from CLover_Ui_Test.clover_app.testcases.test_utils import get_case


class MyAdminSite(admin.AdminSite):
    site_header = '测试工具管理平台'
    site_title = '测试工具管理平台'


@admin.register(PageAction)
class PageActionAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'element_name', 'locate_action')
    list_filter = ('page_name', )


class SceneActionAdmin(admin.TabularInline):
    model = PageScene.scene_actions.through


@admin.register(PageScene)
class PageSceneAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'scene_name', 'scene_description')
    list_filter = ('model_name', )
    inlines = (SceneActionAdmin, )


@admin.register(AppUiCase)
class AppUiCaseAdmin(admin.ModelAdmin):
    list_display = ('project_case', 'case_scene', 'case_name', 'case_description')
    list_filter = ('project_case',)
    actions = [get_case]


@admin.register(ProjectVersion)
class ProjectVersionAdmin(admin.ModelAdmin):
    list_filter = ('project_name', )
