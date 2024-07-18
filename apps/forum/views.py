from django.shortcuts import render, redirect
from django.http import HttpRequest
from . import forms


def index(request: HttpRequest):
    return render(request, 'forum/index.html')


def new_message(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = {
            'form': forms.ForumMessageForm()
        }
        return render(request, 'forum/new_message.html', template_kwargs)

    # Добавление нового сообщения сделать тут
    return redirect( index )
