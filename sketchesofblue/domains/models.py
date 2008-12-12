from django.db import models
from sketchesofblue.customer.models import Customer

# Create your models here.
class Domain(models.Model):
    """
    The domains that we own. When they are due etc.
    """
    domain = models.CharField(max_length=100)
    expires = models.DateField()
    original_cost = models.CharField(blank=True, max_length=100)
    notes = models.TextField(blank=True)
    slug = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        
    def __str__(self):
        return self.domain