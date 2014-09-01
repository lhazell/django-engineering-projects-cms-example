from django.db import models
from project.models import PublicProject

#Contact Form Model
class ContactForm(models.Model):
    name = models.CharField(verbose_name='Main Contact', max_length=49)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    telephone = models.CharField(verbose_name='Telephone', max_length=25, blank=True)
    company_name = models.CharField(verbose_name='Company Name', max_length=28, blank=True)
    message = models.TextField(verbose_name='Message', max_length=1000)
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __unicode__(self):
       return 'message from ' + self.name


#Custom Slider Model
class CustomSlide(models.Model):

    slide_heading = models.CharField(verbose_name='Slide Heading', max_length=23, blank=False)
    slide_sub_heading = models.CharField(verbose_name='Slide Sub-Heading', max_length=49, blank=False)
    slide_intro = models.TextField(verbose_name='Slide Text', blank=False, max_length=231)
    slide_image = models.ImageField(upload_to='images/slider/',max_length=500,blank=False,null=False)
    project_category = models.CharField(max_length=25,
                                      choices=PublicProject.SERVICES
                                      )

    def delete(self, *args, **kwargs):
        storage, path = self.slide_image.storage, self.slide_image.path
        super(CustomSlide, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        permissions = (("readonly", "Can Only Read Projects"),)

    def __unicode__(self):
        return self.slide_heading

