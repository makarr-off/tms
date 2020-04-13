from django.urls import path

from apps.resume.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="resume"),
]