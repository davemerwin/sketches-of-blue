from django.contrib import admin
from sketchesofblue.projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('project_name',)}
    
admin.site.register(Project, ProjectAdmin)