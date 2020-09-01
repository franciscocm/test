"""ZEEV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from ClientManager.views import clientmanager
from CheckinOut.views import checkoutbook, checkinbook, clientbacklog, clientregister, select
#from LoginOut.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('LoginOut.urls')),
    path('', include('ClientManager.urls')),
    #path('checkoutbook', include('CheckinOut.urls')),
    path('checkoutbook', checkoutbook),
    path('checkinbook', checkinbook),
    path('clientbacklog', clientbacklog),
    path('clientregister', clientregister),
    path('clientmanager', clientmanager),
    path('select/', select),
    #path('select/clientregister', clientregister)

    #path('', include('ClientManager.urls')),
    #path('clientRegister_view/', include('clientRegister_view.urls'))
    #path('login', include('register_client.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)