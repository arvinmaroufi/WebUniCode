from django.contrib import messages
from django.shortcuts import render
from django.views import View
from .models import Team
from customer.models import Comment, Newsletter
from project.models import Category


class HomeView(View):
    def get(self, request):
        comments = Comment.objects.filter(publish=True)
        team = Team.objects.last()
        categories = Category.objects.prefetch_related('projects').all()
        return render(request, 'core/home.html', {'comments': comments, 'team': team, 'categories': categories})

    def post(self, request):
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو خبرنامه ما شده اید.')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'ایمیل شما با موفقیت ثبت شد.')
        return render(request, 'core/home.html')


class FaqView(View):
    def get(self, request):
        return render(request, 'core/faq.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'core/contact.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'core/blog.html')
