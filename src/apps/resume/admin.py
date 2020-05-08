from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Project
from apps.resume.models import Responsibility
from apps.resume.models import Technology


@admin.register(Technology)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(Project)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(Responsibility)
class UserInfoAdminModel(ModelAdmin):
    pass
