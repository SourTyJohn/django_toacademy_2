from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.MessageCreationView.as_view(), name='new_message'),
]
