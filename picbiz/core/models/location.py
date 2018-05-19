#directories

from django.db import models
from .section import Section
class Location(models.Model):
    """
    Class to represent Locations
    """

    name                = models.CharField("Name", max_length=255, unique=True)
    section             = models.ForeignKey(Section, related_name='core_loc_section', on_delete=models.DO_NOTHING, default=1)
    lat                 = models.FloatField('Latitude')
    lng                 = models.FloatField('longitude')
    description         = models.CharField("Description", max_length=255, null=True, blank=True)
    created_at          = models.DateTimeField("Created at", auto_now_add=True)
    updated_at          = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
      verbose_name_plural = 'Locations'
