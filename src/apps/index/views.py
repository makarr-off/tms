from django.views.generic import ListView

from apps.index.models import UserInfo


class IndexView(ListView):
    template_name = "index/index.html"
    model = UserInfo

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = UserInfo.objects.first()
        if info is not None:
            ctx = {'title': info.title, 'name': info.name, 'greeting': info.greeting}
            ctx.update(parent_ctx)
        else:
            ctx = parent_ctx

        return ctx
