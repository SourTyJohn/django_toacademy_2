from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='forum_index'),
    path('new_message/', views.Message.as_view(), name='new_message')
]
