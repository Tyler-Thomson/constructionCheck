from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#Login URLs for browsable API
urlpatterns = [
    #Might need these later, so keeping them for the moment
    # url(r'^$', views.login, name='login'),
    # url(r'^profile/$', views.profile, name='profile'),

    #This should employ django-restful's default login/logout urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
