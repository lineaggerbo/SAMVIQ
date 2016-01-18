from django.conf.urls import url
from . import views

app_name = 'evaluations'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<scene_id>[0-9]+)/$', views.scene, name='scene'),
    url(r'^(?P<scene_id>[0-9]+)/rate/$', views.rate, name='rate'),
    url(r'^end/$', views.end, name='end'),
] 