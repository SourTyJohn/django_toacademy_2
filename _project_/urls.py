from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/',  admin.site.urls),
    path('',        include('apps.home.urls')),

    path('users/',  include('apps.users.urls')),
    path('forum/',  include('apps.forum.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
