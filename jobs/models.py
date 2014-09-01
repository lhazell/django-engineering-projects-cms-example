from django.db import models
from django.core.urlresolvers import reverse

from redactor.fields import RedactorField

# Create your models here.
class Job(models.Model):    
    title = models.CharField(verbose_name='Job Title', max_length=49)
    teaser = RedactorField(
        verbose_name=u'Title',
        redactor_options={
        'lang': 'en',
        'focus': 'true',
        'buttons': "['bold', 'italic','unorderedlist', 'orderedlist','alignment']",
        'cleanFontTag': 'true',
        'cleanup': 'true',
        },
        allow_file_upload=False,
        allow_image_upload=False
    )
    description = RedactorField(
        verbose_name=u'Job Description',
        redactor_options={
        'lang': 'en',
        'focus': 'true',
        'buttons': "['html', 'formatting',  'bold', 'italic', 'deleted','unorderedlist', 'orderedlist', 'outdent', 'indent', 'table', 'link', 'alignment', 'horizontalrule']",
        'cleanFontTag': 'true',
        'cleanup': 'true',
        },
        allow_file_upload=False,
        allow_image_upload=False
    )
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)

    class Meta:
        permissions = (("readonly", "Can Only Read Projects"),)

    def get_absolute_url(self):
        return reverse('jobs:job_detail', args=[self.id])

    def __unicode__(self):
       return self.title

