from django.contrib import admin
from sketchesofblue.projects.models import Project

class ProjectsAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Projects, ProjectsAdmin)