# create project urls here
from django.conf.urls import patterns, url
from project.views import ProjectList, ProjectDetail, CategoryProjectList

urlpatterns = patterns('',
    # ex: /project | /projects
    url(r'^$', ProjectList.as_view( template_name="project/projects.html", paginate_by=10 ), name='project_list',),
    # ex: /project/3/
    url(r'^(?P<pk>\d+)/$', ProjectDetail.as_view( template_name="project/detail.html" ), name='project_detail'),
    # ex: /project/transportation | /projects/civil-engineering
    url(r'^category/(?P<category>[-\w]+)/$', CategoryProjectList.as_view(), name='projects_by_category',),
)
