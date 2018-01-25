from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from news.models import News

class NewsView(generic.ListView):
    template_name = 'website/index.html'
    context_object_name = 'news_news'

    def get_queryset(self):
        obj = News.objects.get(pk=1)
