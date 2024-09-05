from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from . import forms


class Index(TemplateView):
    template_name = 'forum/index.html'


class Message(FormView):
    template_name = 'forum/new_message.html'
    success_url = reverse_lazy("forum_index")
    form_class = forms.ForumMessageForm

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        print(form.cleaned_data)
        return super().form_valid(form)
