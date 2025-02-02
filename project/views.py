from django.shortcuts import render
from django.views.generic import DetailView

from .models import Project


class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'project'