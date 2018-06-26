#Customers data
from django.db import models

## Customers joe -->>
        ## Orders1 disk
        ## Order2 email
class Custdata(models.Model):
    """
    Class to represent Customer Data
    """
    name                = models.CharField("Name", max_length=255)
    email               = models.CharField("Email", max_length=255, unique=True)
    phone               = models.CharField("Phone", max_length=20)
    address             = models.CharField("Address", max_length=255)
    address_2           = models.CharField("Address Continued", max_length=255)
    city                = models.CharField("City", max_length=255)
    state               = models.CharField("State", max_length=2)
    city                = models.CharField("City", max_length=255)
    zip                 = models.CharField("Zip", max_length=20)
    notes              = models.CharField("Notes About This Customer", max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
      verbose_name_plural = 'Customers Data'
