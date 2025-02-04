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


class SiteSettings(models.Model):
    about_us_text = models.TextField(null=True, blank=True, verbose_name="متن درباره ما")
    contact_us_text = models.TextField(null=True, blank=True, verbose_name="متن تماس با ما")
    address = models.CharField(max_length=250, null=True, blank=True, verbose_name="آدرس ما")
    phone = models.CharField(max_length=250, null=True, blank=True, verbose_name="تلفن تماس")
    email = models.CharField(max_length=250, null=True, blank=True, verbose_name="ایمیل")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات"


class ContactUs(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=150, verbose_name="ایمیل")
    subject = models.CharField(max_length=100, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    date_send = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")

    class Meta:
        ordering = ["-date_send"]
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.email
