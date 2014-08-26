from django import forms
from project.models import PublicProject, PublicProjectImage
from .models import ContactForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = PublicProject
        exclude = ('created_by',)


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = PublicProjectImage


#from django import forms
#
#class ProjectImageForm(forms.Form):
#    image = forms.FileField(label='Select a profile Image')