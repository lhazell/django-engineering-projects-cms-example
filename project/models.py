from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

from redactor.fields import RedactorField

# Create your models here.
class PublicProject(models.Model):    
    TRANSPORTATION='transportation'
    CONTSTRUCTIONMANAGEMENT='contstruction-management'
    ENVIRONMENTALTESTING='environmental-testing'
    CIVILENGINEERING='civil-engineering'
    ENERGYSYSTEMS='energy-systems'
    MECHANICALENGINEERING='mechanical-engineering'
    SERVICES = (
        (TRANSPORTATION, 'Transportation'),
        (CONTSTRUCTIONMANAGEMENT, 'Contstruction Management'),
        (ENVIRONMENTALTESTING, 'Environmental Testing'),
        (CIVILENGINEERING, 'Civil Engineering'),
        (ENERGYSYSTEMS, 'Energy Systems'),
        (MECHANICALENGINEERING, 'Mechanical Engineering'),
    )

    title = models.CharField(verbose_name='Project Title', max_length=49)
    teaser = models.TextField(verbose_name='Teaser', max_length=350)
    description = RedactorField(
        verbose_name=u'Project Description',
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
    hud_id = models.CharField(
        verbose_name='HUD Id',
        max_length=10,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{3}-[0-9]{6}$',
                message=u'%s is not in pattern 000-000000',
                code='invalid_HUD_Id'
            ),
        ]
    )
    category = models.CharField(max_length=25,
                                      choices=SERVICES
                                      )
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)

    def get_absolute_url(self):
            return reverse('project:project_detail', args=[self.id])

    class Meta:
        ordering = ["-date_created"]
        permissions = (("readonly", "Can Only Read Projects"),)

    def __unicode__(self):
       return self.title


class PublicProjectImage(models.Model):
    project = models.ForeignKey(PublicProject, related_name='images')
    name = models.CharField(verbose_name='Image Description', max_length=140)
    image = models.ImageField(upload_to='images/project/%Y/%m/%d',max_length=500,blank=True,null=True)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(PublicProjectImage, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        permissions = (("readonly", "Can Only Read Projects"),)

    def __unicode__(self):
        return self.name
