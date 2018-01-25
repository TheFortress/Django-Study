from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View

class IndexView(generic.ListView):
    template_name = 'website/index.html'
    context_object_name = 'website_news'

    def get_queryset(self):
        return News.objects.all()
