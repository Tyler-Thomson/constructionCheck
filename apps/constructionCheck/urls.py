from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),


    url(r'^getUsers$', views.getUsers),
    url(r'^createUser$', views.createUser),
    url(r'^showUser/(?P<id>\d+)$', views.showUser),
    url(r'^updateUser/(?P<id>\d+)$', views.updateUser),
    url(r'^destroyUser/(?P<id>\d+)$', views.destroyUser),

    url(r'^getHouses$', views.getHouses),
    url(r'^createHouse$', views.createHouse),
    url(r'^showHouse/(?P<id>\d+)$', views.showHouse),
    url(r'^updateHouse/(?P<id>\d+)$', views.updateHouse),
    url(r'^destroyHouse/(?P<id>\d+)$', views.destroyHouse),

    url(r'^getTypes$', views.getTypes),
    url(r'^createType$', views.createType),
    url(r'^showType/(?P<id>\d+)$', views.showType),
    url(r'^updateType/(?P<id>\d+)$', views.updateType),
    url(r'^destroyType/(?P<id>\d+)$', views.destroyType),

    url(r'^getChecks$', views.getChecks),
    url(r'^createCheck$', views.createCheck),
    url(r'^showCheck/(?P<id>\d+)$', views.showCheck),
    url(r'^updateCheck/(?P<id>\d+)$', views.updateCheck),
    url(r'^destroyCheck/(?P<id>\d+)$', views.destroyCheck),
]
