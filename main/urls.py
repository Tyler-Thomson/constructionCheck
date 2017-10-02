from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^$', serve, kwargs={'path': 'index.html'}),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^', include('apps.constructionCheck.urls')),
]
