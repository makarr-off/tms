from pathlib import Path

from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render


here = Path(__file__).parent.resolve()


def read_static(file, content_type):
    with file.open("rb") as f:
        return HttpResponse(f.read(), content_type)


def view_list(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def view_picture(r):
    return read_static(here.parent.parent / "DSC_0031.png", "image/jpeg")


def view_picture2(r):
    return read_static(here.parent.parent / "our_family.png", "image/jpeg")


def view_resume(request: HttpRequest) -> HttpResponse:
    return render(request, "Resume.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_list),
    path('clone/', view_picture),
    path('Resume/', view_resume),
    path('our_family/', view_picture2),
]