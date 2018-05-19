#directories

from django.db import models


class Company(models.Model):
    """
    Class to represent Locations
    """
    name                = models.CharField("Name", max_length=255, unique=True)
    description         = models.CharField("Description", max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
      verbose_name_plural = 'Companies'
