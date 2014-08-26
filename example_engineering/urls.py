from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from django.contrib import admin



if not settings.configured:
    settings.configure(example_engineering_defaults, DEBUG=True)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project(s)?/', include('project.urls', namespace='project')),
    url(r'^job(s)?/', include('jobs.urls', namespace='jobs')),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^redactor/', include('redactor.urls')),
    #until initial information is added Disallow all [*] robots --- Disallow: /admin
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain"))
 ) + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
