from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('<slug:slug>/', views.ProjectView.as_view(), name='detail_project')
]