from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class PublicPhotos(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    body = models.CharField(max_length=255)
    photo = models.FileField(upload_to='publicphotos/')
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.body

    def get_absolute_url(self):
        #doesnt work!!!!!
        return reverse('publicphotos:detailview', kwargs={'pk': self.pk})
