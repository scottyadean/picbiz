#Customers data
from django.db import models
from .custdata import Custdata
## Customers scott -->>
        ## Orders1 disk
        ## Order2 email

class Order(models.Model):
    """
    Class to represent Orders
    """
    customer_id         = models.ForeignKey(Custdata, related_name='core_custdata', on_delete=models.DO_NOTHING)
    status              = models.CharField("Status", max_length=20, default="open")
    fulfilment          = models.CharField("Fulfilment Type", max_length=255, default="CD")

    use_billing_address = models.BooleanField("Use Billing Address", default=True)
    order_address       = models.CharField("Address", max_length=255, blank=True)
    order_address_2     = models.CharField("Address Continued", max_length=255, blank=True)

    order_city          = models.CharField("City", max_length=255, blank=True)
    order_state         = models.CharField("State", max_length=2, blank=True)
    order_city          = models.CharField("City", max_length=255, blank=True)
    order_zip           = models.CharField("Zip", max_length=20, blank=True)
    order_notes         = models.CharField("Notes About This Customer", max_length=255, null=True, blank=True)

    created_at  = models.DateTimeField("Created at", auto_now_add=True)
    updated_at  = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.status)

    class Meta:
      verbose_name_plural = 'Orders'
