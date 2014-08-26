from django import forms
from project.models import PublicProject, PublicProjectImage


class ProjectForm(forms.ModelForm):
    class Meta:
        model = PublicProject
        exclude = ('created_by',)


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = PublicProjectImage
