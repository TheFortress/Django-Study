from django.conf.urls import url
from . import views

app_name = 'publicphotos'

urlpatterns = [
    url(r'^$', views.photo, name='photo'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.UploadPhoto.as_view(), name='add'),
]
