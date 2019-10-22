from django.urls import include, path
from django.conf.urls import url

from rest_framework import routers
from rest_framework.authtoken import views

from . import admin

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
 #   path('registration/', admin.register)
]
