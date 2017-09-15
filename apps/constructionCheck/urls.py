from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

#Login URLs for browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
