from django.contrib import admin
from project.models import PublicProject, PublicProjectImage


class PublicProjectImageInline(admin.TabularInline):
    model = PublicProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ PublicProjectImageInline]

admin.site.register(PublicProject, ProjectAdmin)
