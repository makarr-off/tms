from django.views.generic import ListView

from apps.index.models import UserInfo


class IndexView(ListView):
    template_name = "index/index.html"
    model = UserInfo
 #   queryset = UserInfo.objects.filter()

  #  def get_context_data(self, **kwargs):
   #     ctx = super().get_context_data(**kwargs)

    #    info = UserInfo.objects.first()
     #   ctx["index"] = info

      #  return ctx
