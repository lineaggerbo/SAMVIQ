from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^evaluations/', include('evaluations.urls')),
    url(r'^admin/', admin.site.urls),
] 