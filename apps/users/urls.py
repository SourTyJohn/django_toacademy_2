from django.urls import path
from .views import UserCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('login/',      UserLoginView.as_view(),  name='login'),
    path('logout/',     UserLogoutView.as_view(), name='logout'),
    path('register/',   UserCreateView.as_view(), name='register')
]
