from django.http import Http404
from django.shortcuts import render
from .models import News

def news(request):
    all_news = News.objects.order_by('date').reverse()[:8]
    return render(request, 'news/index.html', {'all_news': all_news})

def detail(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("Nope")
    return render(request, 'news/detail.html', {'news': news})
