from pathlib import Path

from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render


def view_list(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def view_resume(request: HttpRequest) -> HttpResponse:
    return render(request, "Resume.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_list),
    path('Resume/', view_resume),
]