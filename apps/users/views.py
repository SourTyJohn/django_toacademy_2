from django.shortcuts import render, redirect
from django.http import HttpRequest
import django.contrib.auth as auth
from . import forms


def register(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = {'form': forms.RegisterForm()}
        return render(request, 'users/register.html', template_kwargs)

    register_form = forms.RegisterForm(request.POST)
    if not register_form.is_valid():
        return redirect( register )

    user = register_form.save()
    user.save()
    return redirect( login )


def login(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = { 'form': forms.LoginForm() }
        return render(request, 'users/login.html', template_kwargs)

    login_form = forms.LoginForm(request.POST)

    if not login_form.is_valid():
        pass

    password = login_form.cleaned_data.get('password')
    username = login_form.cleaned_data.get('username')
    user = auth.authenticate(
        request, password=password, username=username
    )

    return redirect( login )
