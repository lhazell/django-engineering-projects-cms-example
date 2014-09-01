from django.conf.urls import patterns, url
from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.contrib.sitemaps import GenericSitemap, FlatPageSitemap
from django.views.generic import TemplateView

from main.views import Index, DymanicCSS, DymanicCSSIe8, ContactView
from project.models import PublicProject
from jobs.models import Job

public_project_dict = {
    'queryset': PublicProject.objects.all(),
    'date_field': 'date_created',
}

jobs_dict = {
    'queryset': Job.objects.all(),
    'date_field': 'date_created',
}

class SitesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    location = "/"

    def items(self):
        return Site.objects.all()


sitemaps = {
    'main': SitesSitemap,
    'projects': GenericSitemap(public_project_dict, priority=0.6),
    'flatpages': FlatPageSitemap,
    'jobs': GenericSitemap(jobs_dict, priority=0.7)
}

urlpatterns = patterns('',
    # ex: / | index.html
    url(r'^(?:|index\.html)$', Index.as_view(), name='main-index',),
    # ex: /css/dynamic-css.css
    url(r'^css/dynamic-css\.css$', DymanicCSS.as_view(content_type="text/css"), name='dynamic-css'),
    # ex: /css/ie8-dynamic-css.css
    url(r'^css/dynamic-css-ie8\.css$', DymanicCSSIe8.as_view(content_type="text/css"), name='dynamic-css-ie8'),
    # ex: /contact
    url(r'^contact/$', ContactView.as_view(), name='main-contact',),
    # ex: /thanks
    url(r'^thanks/', TemplateView.as_view(template_name="main/thanks.html"), name='contact-thanks',),
    # ex: /sitemap.xml
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    # ex: /about-us
    url(r'^about/$', 'flatpage', {'url': '/about-us/'}, name='about'),
    # ex: /privacy
    url(r'^privacy/$', 'flatpage', {'url': '/privacy/'}, name='privacy'),
    # ex: /terms-of-service
    url(r'^terms-of-service/$', 'flatpage', {'url': '/terms-of-service/'}, name='terms-of-service'),
)