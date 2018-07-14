# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('webform/', views.webform, name='webform'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    
]

