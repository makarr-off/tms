from django.views.generic import ListView

from apps.resume.models import Project
from apps.resume.models import Responsibility
from apps.resume.models import Technology


class IndexView(ListView):
    template_name = "resume/index.html"
    queryset = Project.objects.filter()
