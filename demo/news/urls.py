from django.conf.urls import url
from . import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^(?P<news_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<news_id>[0-9]+)/post/$', views.PostComment.as_view(), name='post'),
]
