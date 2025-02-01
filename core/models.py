from django.db import models


class Team(models.Model):
    completed_projects = models.IntegerField(default=0, verbose_name='پروژه های انجام شده')
    satisfied_customers = models.IntegerField(default=0, verbose_name='مشتریان راضی')
    members = models.IntegerField(default=0, verbose_name='تعداد اعضای تیم')
    full_support = models.IntegerField(default=0, verbose_name='پشتیبانی')

    class Meta:
        verbose_name = 'مجموعه'
        verbose_name_plural = 'مجموعه ها'

    def __str__(self):
        return str('شرایط مجموعه')
