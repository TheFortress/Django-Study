from django.conf.urls import url
from . import views

app_name = 'photo'

urlpatterns = [
    url(r'^$', views.photo, name='photo'),
    url(r'^(?P<photo_id>[0-9]+)/$', views.detail, name='detail'),
]
