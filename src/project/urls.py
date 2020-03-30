from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()


def view_name(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())

def view_picture(u):
    picture = here.parent.parent / "img.png"
    with picture.open("rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_name/', view_name),
    path('me/', view_picture)
]
