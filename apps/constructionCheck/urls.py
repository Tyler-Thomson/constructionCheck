from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'houses', views.HouseViewSet)
router.register(r'checklist', views.ChecklistViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'check', views.CheckViewSet)

#Login URLs for browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
]
