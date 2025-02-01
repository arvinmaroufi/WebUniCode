from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('faq', views.FaqView.as_view(), name='faq'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('blog', views.BlogView.as_view(), name='blog'),
]