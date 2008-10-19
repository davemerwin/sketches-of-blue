from django.contrib import admin
from sketchesofblue.customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Customer, CustomerAdmin)