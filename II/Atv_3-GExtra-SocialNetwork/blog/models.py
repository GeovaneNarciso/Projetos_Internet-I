from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    class Meta:
        ordering = ['city']

    def __str__(self):
        return self.city


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='profiles')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
