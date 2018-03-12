from django.db import models
from filebrowser.fields import FileBrowseField
from ckeditor.fields import RichTextField

# Create your models here.

class ModelExample(models.Model):

    img_example = FileBrowseField('Imagen Label',
                                max_length=200, blank=True,
                                extensions=['.jpg', '.png', '.gif'],
                                directory='img_example')

    rich_example = RichTextField("Example", blank=True)

    class Meta:
        verbose_name = "Model Exmaple"
        verbose_name_plural = "Model Examples"

    def __unicode__(self):
        return u"Model Example"

class Photo(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    updated_on = models.DateTimeField("Updated on", auto_now=True)
    title = models.CharField("Title", max_length=255)
    link = models.URLField(
        "Photo Link", max_length=255, help_text="The URL to the image page")
    image_url = models.URLField(
        "Image URL", max_length=255, help_text="The URL to the image file itself")
    description = models.TextField("Description")

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-created_on', 'title']

    def __str__(self):
        return u'A'
