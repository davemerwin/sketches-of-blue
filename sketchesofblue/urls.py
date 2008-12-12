from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sketchesofblue/', include('sketchesofblue.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     
    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    
    # Basic Projects
    # url(r'^projects/', include('sketchesofblue.projects.urls')),
    
    # Admin access only for now
    (r'^(.*)$', admin.site.root),
    
)

# For Static Content Locally - Do Not Use In Production!
if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (settings.PROJECT_PATH)})
    )

