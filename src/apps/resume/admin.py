from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Technology, Responsibility
from apps.resume.models import Project


@admin.register(Technology)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(Project)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(Responsibility)
class UserInfoAdminModel(ModelAdmin):
    pass
