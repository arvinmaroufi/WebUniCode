from django.shortcuts import render
from django.views import View
from customer.models import Comment, Newsletter


class HomeView(View):
    def get(self, request):
        comment = Comment.objects.all()
        return render(request, 'core/home.html', {'comment': comment})

    def post(self, request):
        email = request.POST.get('email')
        Newsletter.objects.create(email=email)
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