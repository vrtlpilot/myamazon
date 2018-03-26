"""lesson1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path

import catalogapp.views as catalogapp
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', catalogapp.main, name='main'),
    re_path(r'^index/', catalogapp.main, name='main'),
    re_path(r'^contacts/', catalogapp.contacts, name='contacts'),
    re_path(r'^catalog/', include('catalogapp.urls', namespace='catalogapp'), name='catalog'),
    re_path(r'^auth/', include('authapp.urls', namespace='authapp'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
