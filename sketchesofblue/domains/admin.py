from django.contrib import admin
from sketchesofblue.domains.models import Domain

class DomainAdmin(admin.ModelAdmin):
    save_on_top = True
    list_filter = ('expires',)
    prepopulated_fields = {'slug': ('domain',)}

admin.site.register(Domain, DomainAdmin)