from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=False)
    body = models.TextField()
    photo = models.FileField(upload_to='news/')

    def __str__(self):
        return self.title + ' - ' + self.body

class NewsComment(models.Model):
    comment = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('website:index')
