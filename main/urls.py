from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.constructionCheck.urls')),
]
