from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    body = models.TextField(max_length=100)
    star = models.IntegerField()
    image = models.ImageField(upload_to='image/customer')

    def __str__(self):
        return f'{self.name} - {self.brand}'


class Newsletter(models.Model):
    email = models.EmailField(max_length=225)

    def __str__(self):
        return self.email