from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=False)
    body = models.TextField()
    photo = models.FileField()

    def get_absolute_url(self):
        return reverse('website:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.body
