from .models import Project
from django.views.generic import DetailView


class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'project'