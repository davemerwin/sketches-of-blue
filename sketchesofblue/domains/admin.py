from django.contrib import admin
from sketchesofblue.domains.models import Domain

class DomainAdmin(admin.ModelAdmin):
    save_on_top = True
    list_filter = ('expires', 'customer',)
    prepopulated_fields = {'slug': ('domain',)}
    list_display = ('domain', 'expires', 'customer',)

admin.site.register(Domain, DomainAdmin)