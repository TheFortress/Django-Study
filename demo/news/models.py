from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=False)
    body = models.TextField()
    photo = models.FileField(upload_to='news/')

    def __str__(self):
        return self.title + ' - ' + self.body
