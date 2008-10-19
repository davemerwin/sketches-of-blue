from django.db import models

# Create your models here.
class Customer(models.Model):
    """
    The basic contact information for the customer. This can be expanded quite a bit.
    """
    name = models.CharField(blank=True, max_length=200)
    contact_email = models.EmailField()
    website = models.URLField(blank=True, verify_exists=True)
    phone = models.CharField(blank=True, max_length=100)
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        
    def __str__(self):
        return self.name