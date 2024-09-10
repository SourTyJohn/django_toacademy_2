from django.views.generic import TemplateView
from apps.forum.models import ForumMessage


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = kwargs
        context["messages"] = ForumMessage.get_all()
        return super(Index, self).get_context_data(**context)
