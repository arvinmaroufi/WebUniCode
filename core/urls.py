from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('faq', views.FaqView.as_view(), name='faq'),
    path('contact', views.ContactView.as_view(), name='contact'),
]