from django.db import models


class Account(models.Model):
    owner = models.CharField(max_length=200, blank=True, default='')
    balance = models.FloatField()
    creation_date = models.DateField(auto_now_add=True)
