from  django.db import models
from taggit.managers import TaggableManager

from .directory import Directory
from .location import Location
from .company import Company
from .section import Section

class Mainfest(models.Model):
    """
    Class to represent List of dir. objects
    """
    name          = models.CharField("name", max_length=255)
    caption       = models.CharField("Caption", max_length=255, null=True, blank=True)
    subject       = models.CharField("Subject", max_length=255, default='', null=True, blank=True)

    directory     = models.ForeignKey(Directory, related_name='core_dir', on_delete=models.DO_NOTHING)
    location      = models.ForeignKey(Location, related_name='core_loc', on_delete=models.DO_NOTHING, default=1)
    section       = models.ForeignKey(Section, related_name='core_section', on_delete=models.DO_NOTHING, default=1)
    company       = models.ForeignKey(Company, related_name='core_company', on_delete=models.DO_NOTHING, default=1)

    import_status = models.CharField("Import Status", max_length=255, default='init' )

    exif_datetime = models.DateField("exif_date", null=True, blank=True)
    exif_height   = models.CharField("exif_height", max_length=255, null=True, blank=True )
    exif_width    = models.CharField("exif_width", max_length=255, null=True, blank=True )

    lat          = models.FloatField("lat", default=0)
    lng          = models.FloatField("lng", default=0)

    meta_1       = models.CharField("meta_1", max_length=255, default="", null=True, blank=True )
    meta_2       = models.CharField("meta_2", max_length=255, default="", null=True, blank=True )
    meta_3       = models.CharField("meta_3", max_length=255, default="", null=True, blank=True )

    tags         = TaggableManager()

    created_at  = models.DateTimeField("Created at", auto_now_add=True)
    updated_at  = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.name)


    class Meta:
      pass
