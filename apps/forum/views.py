from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms


class MessageCreationView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('login')

    template_name = 'new_message.html'
    success_url = reverse_lazy("index")
    form_class = forms.ForumMessageForm

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        return super().form_valid(form)
