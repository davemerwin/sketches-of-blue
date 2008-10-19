from django.db import models

# Create your models here.
class Customer(models.Model):
    """
    The basic contact information for the customer.
    """
    
class Project(models.Model):
    """
    The customer's project. Customers can have many projects. Each project's sett8ings are stored here.
    
    In the future it will be nice to have a way to display and protect passwords.
    
    Most everything will be imported to here. This is the primary view for content.
    
    Import: Customer, Domains, Sub Domains, Hosting Plan and Host
    """
