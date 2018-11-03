from django.shortcuts import get_object_or_404, render

from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def all_projects_index(request):
    project_list = Project.objects.all()
    context = {'project_list':project_list}
    return render(request, 'ProjectDocsSiteApp/all_projects_index.html', context)

@login_required
def all_projects_map(request):
    project_list = Project.objects.all()
    context = {'project_list':project_list}
    return render(request, 'ProjectDocsSiteApp/all_projects_map.html', context)

@login_required 
def project(request, project_id):
    project_data = get_object_or_404(Project, pk=project_id)
    context = {'project_data':project_data}
    return render(request, 'ProjectDocsSiteApp/project.html', context) 
    