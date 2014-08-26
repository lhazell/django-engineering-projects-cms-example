# create project urls here
from django.conf.urls import patterns, url
from jobs.views import JobList, JobDetail

urlpatterns = patterns('',
    # ex: /job | /jobs
    url(r'^$', JobList.as_view( template_name="jobs/jobs.html", paginate_by=10 ), name='jobs_list',),
    # ex: /project/3/
    url(r'^(?P<pk>\d+)/$', JobDetail.as_view( template_name="jobs/detail.html" ), name='job_detail'),
)
