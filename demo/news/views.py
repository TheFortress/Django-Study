from django.http import Http404
from django.shortcuts import render
from .models import News, NewsComment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View

def news(request):
    all_news = News.objects.order_by('date').reverse()[:8]
    return render(request, 'news/index.html', {'all_news': all_news})

def detail(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("Nope")
    return render(request, 'news/detail.html', {'news': news})

class PostComment(CreateView):
    model = NewsComment
    fields = ['comment', 'news']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)
