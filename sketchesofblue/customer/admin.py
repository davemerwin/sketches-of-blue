from django.contrib import admin
from sketchesofblue.customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    save_on_top = True

admin.site.register(Customer, CustomerAdmin)