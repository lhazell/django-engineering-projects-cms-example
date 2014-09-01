# ex: / - Index
import json
import logging

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

from project.models import PublicProject
from main.models import CustomSlide

from google.appengine.ext import blobstore
from google.appengine.api import images
from google.appengine.api import mail


from .forms import ContactForm

class Index(TemplateView):
    template_name = "main/index.html"
    form_class = ContactForm
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['slides'] = CustomSlide.objects.all()
        context['latest_projects'] = PublicProject.objects.all()[:15]
        return context

    def url(self, name):
        """
        Ask blobstore api for an url to directly serve the file
        """
        key = blobstore.create_gs_key('/gs' + name)
        return images.get_serving_url(key)


class ContactView(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        data = {
            'message' : '',
            'status' : '',
            'errors' : ''
        }

        #get admin email accounts
        adminEmails = []
        admins = User.objects.all().filter(groups__name='Administrators')

        for admin in admins:
            adminEmails.append(admin.email)

        #get message variables
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # <process form cleaned data>
        new_contactFormSubmission = self.form_class(form.cleaned_data)
        new_contactFormSubmission.save()

        try:
            mail.send_mail(sender='' + name + '<' + email + '>',
                          to = adminEmails,
                          subject = "New e-mail from ebsengineering.com",
                          body = message)
        except:
            logging.error('ERROR: Invalid header.')

            if self.request.is_ajax():
                data['message'] = 'ERROR: Invalid header.',
                data['status'] = 'error'

                return HttpResponse(json.dumps(data), content_type = "application/json")
            else:
                raise Exception
        
        # Only executed with jQuery form request
        if self.request.is_ajax():

            data['message'] = 'Thank You. Your message has been sent.',
            data['status'] = 'success'

            return HttpResponse(json.dumps(data), content_type = "application/json")
        else:
            return super(ContactView, self).form_valid(form)


    def form_invalid(self, form):
        data = {
            'message' : '',
            'status' : '',
            'errors' : ''
        }

        if self.request.is_ajax():
            errors = {}

            # Prepare JSON for parsing
            data['message'] = 'Error, Bad input; please re-submit.'
            data['status'] = 'error'

            if form.errors:
                for error in form.errors:
                    e = form.errors[error]

                    errors[error] = unicode(e)

                data['errors'] = errors

            return HttpResponseBadRequest(json.dumps(data))
        else:
            return super(ContactView, self).form_invalid(form)

#Create dynamic Stylesheet for Slides
class DymanicCSS(TemplateView):
    template_name="main/css/dynamic-css.css"

    def get_context_data(self, **kwargs):
        context = super(DymanicCSS, self).get_context_data(**kwargs)
        context['slides'] = CustomSlide.objects.all()
        return context

    def url(self, name):
        """
        Ask blobstore api for an url to directly serve the file
        """
        key = blobstore.create_gs_key('/gs' + name)
        return images.get_serving_url(key)

#Create dynamic Stylesheet for IE8 Slides
class DymanicCSSIe8(TemplateView):
    template_name="main/css/dynamic-css-ie8.css"

    def get_context_data(self, **kwargs):
        context = super(DymanicCSS, self).get_context_data(**kwargs)
        context['slides'] = CustomSlide.objects.all()
        return context

    def url(self, name):
        """
        Ask blobstore api for an url to directly serve the file
        """
        key = blobstore.create_gs_key('/gs' + name)
        return images.get_serving_url(key)