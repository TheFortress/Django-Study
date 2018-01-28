from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
    photo = models.FileField(upload_to='photo/')

    def __str__(self):
        return self.title + ' - ' + self.body
