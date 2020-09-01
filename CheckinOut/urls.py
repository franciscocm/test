from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
#from ClientManager.views import clientmanager
urlpatterns = [
    path('checkoutbook/',views.checkoutbook, name='checkoutbook'),
    path('checkinbook/',views.checkinbook, name='checkinbook'),
    path('clientbacklog/',views.clientbacklog, name='clientbacklog'),
    path('clientregister/',views.clientregister, name='clientregister'),
    path('select/',views.select, name='select'),
    path('select/clientregister/',views.clientregister, name='select'),
    #path('',clientmanager, name='clientmanager'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)