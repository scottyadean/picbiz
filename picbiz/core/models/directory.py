#directories

from django.db import models
from slugify import slugify

class Directory(models.Model):
    """
    Class to represent Directory
    """
    name                = models.CharField("Name", max_length=255, unique=True)
    full_path           = models.CharField("Full Path", max_length=255, unique=True)
    slug                = models.CharField("Slug", max_length=255)
    status              = models.CharField("Status", max_length=50)
    description         = models.CharField("Description", max_length=255, null=True, blank=True)
    file_count          = models.IntegerField('File Count', default=0 )
    create_by           = models.CharField("Created By", max_length=255, null=True, blank=True)
    created_at          = models.DateTimeField("Created at", auto_now_add=True)
    updated_at          = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Directory, self).save(*args, **kwargs)


    class Meta:
      verbose_name_plural = 'Directories'
