# Create your views here.
from django.views.generic import ListView, DetailView
from jobs.models import Job


# ex: /job/ | /jobs - List
class JobList(ListView):
    model = Job
    context_object_name = 'jobs'


# ex: /job/1/ - Detail
class JobDetail(DetailView):
    model = Job
    context_object_name = 'job_detail'
