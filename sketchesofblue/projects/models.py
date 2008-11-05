from django.db import models
from sketchesofblue.customer.models import Customer
from sketchesofblue.domains.models import Domain
from sketchesofblue.host.models import Company, Plan

# Create your models here.
class Project(models.Model):
    """
    The customer's project. Customers can have many projects. Each project's sett8ings are stored here.
    
    In the future it will be nice to have a way to display and protect passwords.
    
    Most everything will be imported to here. This is the primary view for content.
    
    Import: Customer, Domains, Sub Domains, Hosting Plan and Host
    """
    project_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    domains = models.ManyToManyField(Domain)
    host_company = models.ForeignKey(Company)
    host_plan = models.ForeignKey(Plan)
    notes = models.TextField(blank=True)
    slug = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
    def __str__(self):
        return self.name