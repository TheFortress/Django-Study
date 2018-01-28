from django.http import Http404
from django.shortcuts import render
from .models import Photo

def photo(request):
    all_photos = Photo.objects.order_by('date').reverse()
    return render(request, 'photo/index.html', {'all_photos': all_photos})

def detail(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404("Nope")
    return render(request, 'photo/detail.html', {'photo': photo})
