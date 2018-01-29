from django.http import Http404
from django.shortcuts import render
from news.models import News
from photo.models import Photo
from publicphotos.models import PublicPhotos
from django.contrib.auth.models import User


def index(request):
    news = News.objects.order_by('date').reverse()[:1]
    recent_photos = Photo.objects.order_by('id').reverse()[:9]
    recent_publicphotos = PublicPhotos.objects.order_by('id').reverse()[:9]
    recent_users = User.objects.order_by('date_joined').reverse()[:20]
    context = {
        'news': news,
        'recent_photos': recent_photos,
        'recent_publicphotos':recent_publicphotos,
        'recent_users':recent_users,
    }
    return render(request, 'website/index.html', context)
