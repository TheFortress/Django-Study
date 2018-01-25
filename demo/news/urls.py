from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.NewsView.as_view(), name='index'),
]
