from django.db import models


class Post(models.Model):
    pass


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'short'),
        ('M', 'medium'),
        ('L', 'large')
    )

    first_name = models.CharField(max_length=30)
    midle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, null=True)
