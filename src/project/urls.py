from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()


def read_static(file, content_type):
    with file.open() as f:
        return HttpResponse(f.read(), content_type)


def view_list(r):
    name = here.parent.parent / "index.html"
    return read_static(name, content_type=None)


def view_picture(u):
    name = here.parent.parent / "img1.png"
    return read_static(name, content_type="image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_list),
    path('img1/', view_picture),
]
