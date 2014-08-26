import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.forms import ModelForm
from project.models import PublicProject, PublicProjectImage
from django.views.generic.base import View

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


class ProjectForm(ModelForm):
    class Meta:
        model = PublicProject

def index(request):
    form = ProjectForm()

    if request.method == 'POST': # If the form has been submitted...
        form = ProjectForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ProjectForm() # An unbound form

    return render(request, 'project/index.html', {
        'form': form,
    })



class ImageForm(ModelForm):
    class Meta:
        model = PublicProjectImage

class Upload(View, blobstore_handlers.BlobstoreUploadHandler):
    form_class = ImageForm
    template_name = 'project/upload.html'
    today = datetime.datetime.now()
    template = loader.get_template('project/upload.html')



    def get(self, request, *args, **kwargs):
        upload_url = blobstore.create_upload_url('/project/upload/', gs_bucket_name='ebs-engineering-uploads/images/project/' + self.today.strftime("%Y/%m/%d") + '/')
        context = RequestContext(request, {
            'form': self.form_class,
            'upload_url': upload_url,
        })
        return HttpResponse(self.template.render(context))

    def post(self, request, *args, **kwargs):
        template = loader.get_template('project/image.html')

        form = self.form_class(request.POST)
        if form.is_valid():
            file_info = self.get_file_infos()[0]
            context = RequestContext(request, {
                    'image': file_info,
                })
            return HttpResponse(template.render(context))
            #return HttpResponseRedirect(serving_url)

        return render(request, self.template_name, {'form': form})



#def index(request):
#    upload_url = blobstore.create_upload_url('project/upload')
#
#    latest_project_list = PublicProject.objects.order_by('-date_created')[:5]
#    template = loader.get_template('project/index.html')
#    context = RequestContext(request, {
#        'latest_project_list': latest_project_list,
#        'upload_url': upload_url,
#    })
#    return HttpResponse(template.render(context))

#Add, Detail, Edit