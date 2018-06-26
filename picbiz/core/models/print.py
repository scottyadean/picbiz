#Customers data
from django.db import models
from .order import Order
from .manifest import Manifest
class Print(models.Model):
    """
    Class to represent Orders Prints
    """
    order_id    = models.ForeignKey(Order, related_name='core_print_order', on_delete=models.DO_NOTHING)
    manifest_id = models.ForeignKey(Manifest, related_name='core_print_manifest', on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return str(self.order_id)

    class Meta:
      verbose_name_plural = 'Prints'
