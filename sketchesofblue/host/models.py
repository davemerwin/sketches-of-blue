from django.db import models

# Create your models here.
class Company(models.Model):
    """
    This is the company that hosts the website. Basic contact information is listed.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ('Type')
        verbose_name_plural = ('Type')
    
    def __str__(self):
        return self.name
        
class Plan(models.Model):
    """
    The plan that the hosting company provides. Simple information like price, bandwidth and storage amount.
    
    This should be update occasionally by looking at the site's info.
    """        