from django.db import models

# Create your models here.
class Company(models.Model):
    """
    This is the company that hosts the website. Basic contact information is listed.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True, verify_exists=True)
    support_email = models.EmailField()
    support_forums = models.URLField(blank=True, verify_exists=True)
    extra_service_notes = models.TextField(blank=True, help_text="What other services does this company provide and what are the fees?")
    
    class Meta:
        verbose_name = ('Company')
        verbose_name_plural = ('Companies')
    
    def __str__(self):
        return self.name
        
class Plan(models.Model):
    """
    The plan that the hosting company provides. Simple information like price, bandwidth and storage amount.
    
    This should be update occasionally by looking at the site's info.
    
    Foriegn Key Brings in the Company
    """
    host = models.ForeignKey(Company)
    plan_name = models.CharField(max_length=100)
    yearly_discount_available = models.BooleanField(default=False)
    current_price = models.DecimalField(max_digits=6, decimal_places=2, help_text="What is the price that you are paying.")
    billed_price = models.DecimalField(blank=True, max_digits=6, decimal_places=2, help_text="What is the price that your customer is paying.")
    disk_space = models.CharField(blank=True, max_length=100)
    bandwidth = models.CharField(blank=True, max_length=100)
    memory = models.CharField(blank=True, max_length=100)
    
    def __str__(self):
        return self.name