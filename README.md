# 1. начальные настройки

Установить poetry 
```shell
pip install poetry
```

Создать файл poetry для проекта
```shell
poetry init
```

Установить django через poetry
```shell
poetry add django
```

# 2. создание проекта
Создать django-проект
```shell
django-admin startproject _project_ .
```

```text
После этого создаем папку apps рядом с _project_
В этой папке будут лежать все приложения (app) проекта
```

Создать django-приложение
```shell
django-admin startprapp название_приложения
```

```text
Это приложение надо переместить в папку apps
И в файле "apps.название_приложения.apps.py" дописать "apps." в переменной name
```

```python
# apps.py
from django.apps import AppConfig

class IndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.index'
```

Добавить приложение в список приложений в project/settings.py
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'название_приложения ( как name в файле apps.py приложения )'
]
```

В project создать папку templates, в которой будут храниться шаблоны, и указать эту папку в настройках проекта.
* шаблоны (templates) - это название для .html файлов

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["_project_/templates"],  # <-- указать папку для html файлов
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


# 3. настройка приложения

В файл views.py добавить функцию с аргументом request. 
Это будет наш вид (вьюха). index в примере отобразит пользователю содержимое файла index.html, котороый должен располагаться в папке templates.

```python
# apps/приложение/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

Создать в приложении файл urls.py
```python
# apps/приложение/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('путь/', views.название_вида),
    ...
]
```

В корневом файле urls.py, который лежит в project добавить наше приложение
```python
# _project_/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('путь_к_приложению/', include('apps.index.urls'))
]
```

В итоге путь до вида, будет иметь вид: http://127.0.0.1/путь_к_приложению/путь_к_виду
