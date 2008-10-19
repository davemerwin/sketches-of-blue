from django.db import models

# Create your models here.
class Domain(models.Model):
    """
    The domains that we own. When they are due etc.
    """
    domain_name = models.CharField(blank=True, max_length=200)
    expires = models.DateField()
    original_cost = models.CharField(blank=True, max_length=100)
    
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        
    def __str__(self):
        return self.domain_name