from django.conf.urls import url
from . import views
from django.conf import settings

app_name = 'account'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
]
