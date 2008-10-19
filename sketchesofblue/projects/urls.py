from sketchesofblue.customer.models import Customer
from sketchesofblue.domains.models import Domain
from sketchesofblue.host.models import Company, Plan
from sketchesofblue.projects.models import Project
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

def project_list(request):
    project = Project.objects.all()