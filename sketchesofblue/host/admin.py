from django.contrib import admin
from sketchesofblue.host.models import Company, Plan

class CompanyAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Company, CompanyAdmin)

class PlanAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('plan_name',)}

admin.site.register(Plan, PlanAdmin)