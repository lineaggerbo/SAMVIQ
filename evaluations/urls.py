from django.conf.urls import url
from . import views

app_name = 'evaluations'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tutorial/$', views.tutorial, name='tutorial'),
    url(r'^testscene/$', views.testscene, name='testscene'),
    url(r'^info/$', views.info, name='info'),
    url(r'^scene/(?P<scene_id>[1-9]+)/$', views.scene, name='scene'),
    url(r'^scene/(?P<scene_id>[1-9]+)/rate/$', views.rate, name='rate'),
    url(r'^end/$', views.end, name='end'),
    url(r'^end-nopa/$', views.end_nopa, name='end-nopa'),
] 