from django.contrib import admin
from django.urls import path, include

#from graphene_django_views import GraphQLView
from django.conf.urls import include

from rest_framework import routers
from rest_framework.authtoken import views

#router = routers.DefaultRouter()
#router.register('adventure', )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    # To DEl later
    path('api-token-auth/', views.obtain_auth_token)
]
