from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^$', serve, kwargs={'path': 'index.html'}),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('apps.constructionCheck.urls')),
]
