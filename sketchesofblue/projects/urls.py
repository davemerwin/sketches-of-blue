from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list
from sketchesofblue.projects.models import Project

project_list = {
    'queryset': Project.objects.all(),
    'paginate_by': 25,
}

project_object = {
    'queryset': Project.objects.all(),
    'slug_field': 'slug',
}

urlpatterns = patterns('',
    # Project List
    #url(r'^$', include('sketchesofblue.projects.urls')),
    
    # For the profiles for users
    url(r'^(?P<slug>[-\w]+)/$', 'django.views.generic.list_detail.object_detail', dict(project_object)),
    
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(project_list))
)