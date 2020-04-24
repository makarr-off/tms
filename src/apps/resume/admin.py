from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Technology, Responcibility
from apps.resume.models import Project



@admin.register(Technology)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(Project)
class UserInfoAdminModel(ModelAdmin):
    pass

@admin.register(Responcibility)
class UserInfoAdminModel(ModelAdmin):
    pass

