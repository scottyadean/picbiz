
from  django.db import models

class UI(models.Model):
    """
    Class to hold UI elemets
    """
    name        = models.CharField("Name", max_length=255)
    type        = models.CharField("Type", max_length=255, null=True, blank=True)
    markup      = models.CharField('Markup', max_length=225, null=True, blank=True )
    group       = models.CharField('Group', max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
      pass
