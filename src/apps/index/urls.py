from django.urls import path

from apps.index.views import view_list

urlpatterns = [
    path('', view_list),
]