from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path, include
from django.shortcuts import render


def view_resume(request: HttpRequest) -> HttpResponse:
    return render(request, "Resume.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.index.urls')),
    path('Resume/', view_resume),
]