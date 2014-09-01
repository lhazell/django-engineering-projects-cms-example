from django.contrib import admin
from .models import ContactForm, CustomSlide

admin.site.register(ContactForm)

class customSlideAdmin(admin.ModelAdmin):
    pass

class ReadonlyProjectAdmin(customSlideAdmin):
    def __init__(self, model, admin_site):
      super(ReadonlyProjectAdmin, self).__init__(model, admin_site)
      self.model = model

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('project.readonly') and not request.user.is_superuser:
            return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.has_perm('project.readonly') and not request.user.is_superuser:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = () # make sure to remove caching.
            return True
        elif request.user.has_perm('project.readonly'):
            # make the fields readonly for only users with readonly permissions.
            self.readonly_fields = [field.name for field in filter(lambda f: not f.auto_created, self.model._meta.fields)]
            return True
        else:
            return False


    def get_actions(self, request):
        actions = super(ReadonlyProjectAdmin, self).get_actions(request)
        if request.user.has_perm('project.readonly') and not request.user.is_superuser:
            # This ensures that that user doesn't not have any actions
            if 'delete_selected' in actions:
                del actions['delete_selected']
                print "I deleted delete_selected"
            if 'accept' in actions:
                del actions['accept']
                print "I deleted accept"
            if 'reject' in actions:
                del actions['reject']
                print "I deleted reject"
            if 'pending' in actions:
                del actions['pending']
                print "I deleted pending"
            return actions
        else:
            return actions

admin.site.register(CustomSlide, ReadonlyProjectAdmin)


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