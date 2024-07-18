from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'password', 'email')

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
            'email': 'Электронная почта'
        }
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput()
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'password' )

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
        }
