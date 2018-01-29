from django.http import Http404
from django.shortcuts import render
from .models import PublicPhotos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View

def photo(request):
    publicphotos = PublicPhotos.objects.order_by('id').reverse()
    return render(request, 'publicphotos/index.html', {'publicphotos': publicphotos})

class DetailView(generic.DetailView):
    model = PublicPhotos
    template_name = 'publicphotos/detail.html'

#def detail(request, publicphotos_id):
#    try:
#        publicphotos = PublicPhotos.objects.get(pk=publicphotos_id)
#    except PublicPhotos.DoesNotExist:
#        raise Http404("Nope")
#    return render(request, 'publicphotos/detail.html', {'publicphotos': publicphotos})

class UploadPhoto(CreateView):
    model = PublicPhotos
    fields = ['title', 'body', 'photo']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)
