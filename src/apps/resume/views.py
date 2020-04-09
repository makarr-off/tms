from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_resume(request: HttpRequest) -> HttpResponse:
    return render(request, "resume/Resume.html")