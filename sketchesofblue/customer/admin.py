from django.contrib import admin
from sketchesofblue.customer.models import Customer
from sketchesofblue.projects.models import Project
from sketchesofblue.domains.models import Domain

class ProjectInline(admin.TabularInline):
    model = Project
    
class DomainInline(admin.TabularInline):
    model = Domain

class CustomerAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProjectInline, DomainInline,]
    list_display = ('name', 'phone', 'contact_email', 'website')

admin.site.register(Customer, CustomerAdmin)