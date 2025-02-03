from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='نامک', null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='نامک')
    name = models.CharField(max_length=100, verbose_name='نام مشتری')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    budget = models.CharField(max_length=100, verbose_name='بودجه')
    project_manager = models.CharField(max_length=60, verbose_name='مدیر پروژه')
    place = models.CharField(max_length=100, verbose_name='محل')
    website = models.URLField(max_length=200, verbose_name='وب سایت')
    star = models.IntegerField(verbose_name='امتیاز')
    main_image = models.ImageField(upload_to='project', verbose_name='عکس اصلی')
    image1 = models.ImageField(upload_to='project', verbose_name='عکس 1')
    image2 = models.ImageField(upload_to='project', verbose_name='عکس 2')
    Text1 = models.TextField(verbose_name='متن یک, توضیحات')
    Text2 = models.TextField(verbose_name='متن دو, نکات پروژه')
    Text3 = models.TextField(verbose_name='متن سوم, نمای کلی و چالش ها')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return f"{self.name} - {self.website}"
