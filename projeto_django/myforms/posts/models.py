from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=280)
    editable = models.BooleanField(default=False)
    data_published = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.title
