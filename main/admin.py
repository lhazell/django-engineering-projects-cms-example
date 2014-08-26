from django.contrib import admin
from .models import ContactForm, CustomSlide

admin.site.register(ContactForm)
admin.site.register(CustomSlide)


"""
Redactorjs: http://redactorjs.com/
django-redactorjs: https://github.com/TigorC/django-redactorjs
"""

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm as OldFlatpageForm
 
from redactor.widgets import RedactorEditor
 
class FlatpageForm(OldFlatpageForm):
    class Meta:
        model = FlatPage
        widgets = {
           'content': RedactorEditor(),
        }
 
class FlatPageAdmin(OldFlatPageAdmin):
    form = FlatpageForm
 
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)