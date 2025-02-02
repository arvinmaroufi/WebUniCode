from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    body = models.TextField(max_length=100)
    star = models.IntegerField()
    image = models.ImageField(upload_to='image/customer')
    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.name} - {self.brand}'


class Newsletter(models.Model):
    email = models.EmailField(max_length=225)

    class Meta:
        verbose_name = 'خبرنامه'
        verbose_name_plural = 'خبرنامه ها'

    def __str__(self):
        return self.email
