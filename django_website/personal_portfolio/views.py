from django.shortcuts import render
from projects.models import Project
from django.core.cache import caches
from access import query

# Create your views here.

def my_view(request):
    result = query("New York")
    return render(request, "index.html",{'result' : result}
    


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


