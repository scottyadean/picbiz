


from  django.db import models


class Section(models.Model):
    """
    Class to Section
    """
    name        = models.CharField("Header", max_length=255)
    description = models.CharField("Description", max_length=255, null=True, blank=True)
    region      = models.CharField('Region', max_length=225, null=True, blank=True )


    def __str__(self):
        return str(self.name)


    class Meta:
      pass
