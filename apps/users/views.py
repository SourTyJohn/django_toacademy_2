from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from utils.mixins import SaveValidFormMixin


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy("index")
    success_message = "Вход успешен!"


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = "Вы вышли из аккаунта!"


class UserCreateView(SuccessMessageMixin, SaveValidFormMixin, FormView):
    template_name = 'register.html'
    success_message = "Вы успешно зарегестрировались"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
