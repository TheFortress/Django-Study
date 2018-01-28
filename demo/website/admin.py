from django.contrib import admin
from news.models import News
from photo.models import Photo
from publicphotos.models import PublicPhotos

admin.site.register(News)
admin.site.register(Photo)
admin.site.register(PublicPhotos)
