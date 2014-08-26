#from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_list_or_404
from django.views.generic import ListView, DetailView

from project.models import PublicProject


# ex: /project/ | /projects - List
class ProjectList(ListView):
    model = PublicProject
    context_object_name = 'projects'

# ex: /project/ | /projects - List
class CategoryProjectList(ListView):
    model = PublicProject
    context_object_name = 'projects'
    template_name="project/projects.html"
    paginate_by=10

    def get_queryset(self):
        #projects = PublicProject.objects.all().filter(category__title=self.kwargs['category'])
        projects = get_list_or_404(PublicProject, category=self.kwargs['category'])
        return projects

# ex: /project/3/ - Detail
class ProjectDetail(DetailView):
    model = PublicProject
    context_object_name = 'project_detail'
